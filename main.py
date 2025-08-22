from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel, ConfigDict
from instagrapi import Client
import os
import json
from typing import Optional, List, Annotated
from pathlib import Path
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# API Key Authentication
def verify_api_key(x_api_key: Annotated[str, Header()]):
    expected_api_key = os.getenv("APP_API_KEY")
    if not expected_api_key:
        raise HTTPException(status_code=500, detail="API key not configured on server")
    if x_api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return True

app = FastAPI(title="Instagram DM API", description="Send Instagram DMs using instagrapi")

sessions_dir = Path("./sessions")
sessions_dir.mkdir(exist_ok=True)

class LoginRequest(BaseModel):
    verification_code: Optional[str] = None

class DMRequest(BaseModel):
    recipient_username: str
    message: str

class BulkDMRequest(BaseModel):
    recipient_usernames: List[str]
    message: str

class AuthResponse(BaseModel):
    success: bool
    message: str
    session_id: Optional[str] = None
    requires_2fa: Optional[bool] = False
    challenge_required: Optional[bool] = False

class DMResponse(BaseModel):
    success: bool
    message: str
    failed_recipients: Optional[List[str]] = None

class ThreadsResponse(BaseModel):
    success: bool
    threads: List[dict]
    message: str

class MessagesResponse(BaseModel):
    success: bool
    messages: List[dict]
    message: str

def get_session_file(username: str) -> Path:
    return sessions_dir / f"{username}_session.json"

def save_session(client: Client, username: str):
    session_file = get_session_file(username)
    session_data = client.get_settings()
    with open(session_file, 'w') as f:
        json.dump(session_data, f)

def load_session(username: str) -> Optional[dict]:
    session_file = get_session_file(username)
    if session_file.exists():
        with open(session_file, 'r') as f:
            return json.load(f)
    return None

@app.post("/auth/login", response_model=AuthResponse)
async def login(request: LoginRequest, api_key: bool = Depends(verify_api_key)):
    try:
        username = os.getenv("INSTAGRAM_USERNAME")
        password = os.getenv("INSTAGRAM_PASSWORD")
        
        if not username or not password:
            raise HTTPException(status_code=400, detail="Instagram credentials not found in environment")
        
        cl = Client()
        
        session_data = load_session(username)
        if session_data:
            cl.set_settings(session_data)
            try:
                if request.verification_code:
                    cl.login(username, password, verification_code=request.verification_code)
                else:
                    cl.login(username, password)
                save_session(cl, username)
                return AuthResponse(
                    success=True,
                    message="Logged in successfully using existing session",
                    session_id=username
                )
            except Exception as e:
                if "two_factor_required" in str(e) or "checkpoint_challenge_required" in str(e):
                    return AuthResponse(
                        success=False,
                        message="2FA verification code required",
                        requires_2fa=True
                    )
                elif "challenge_required" in str(e):
                    return AuthResponse(
                        success=False,
                        message="Account challenge required - check Instagram app",
                        challenge_required=True
                    )
        
        if request.verification_code:
            cl.login(username, password, verification_code=request.verification_code)
        else:
            cl.login(username, password)
        
        save_session(cl, username)
        
        return AuthResponse(
            success=True,
            message="Logged in successfully",
            session_id=username
        )
    
    except Exception as e:
        error_str = str(e).lower()
        if "two_factor_required" in error_str or "checkpoint_challenge_required" in error_str:
            return AuthResponse(
                success=False,
                message="2FA verification code required. Please provide verification_code in your request.",
                requires_2fa=True
            )
        elif "challenge_required" in error_str:
            return AuthResponse(
                success=False,
                message="Account challenge required. Please check your Instagram app and approve the login attempt.",
                challenge_required=True
            )
        else:
            raise HTTPException(status_code=400, detail=f"Login failed: {str(e)}")

@app.post("/dm/send", response_model=DMResponse)
async def send_dm(request: DMRequest, session_id: str, api_key: bool = Depends(verify_api_key)):
    try:
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        cl = Client()
        cl.set_settings(session_data)
        
        user_id = cl.user_id_from_username(request.recipient_username)
        cl.direct_send(request.message, [user_id])
        
        return DMResponse(
            success=True,
            message=f"DM sent successfully to {request.recipient_username}"
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to send DM: {str(e)}")

@app.post("/dm/send-bulk", response_model=DMResponse)
async def send_bulk_dm(request: BulkDMRequest, session_id: str, api_key: bool = Depends(verify_api_key)):
    try:
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        cl = Client()
        cl.set_settings(session_data)
        
        failed_recipients = []
        successful_count = 0
        
        for username in request.recipient_usernames:
            try:
                user_id = cl.user_id_from_username(username)
                cl.direct_send(request.message, [user_id])
                successful_count += 1
            except Exception as e:
                failed_recipients.append(username)
        
        if successful_count == 0:
            return DMResponse(
                success=False,
                message="Failed to send DM to all recipients",
                failed_recipients=failed_recipients
            )
        
        message = f"DM sent successfully to {successful_count} recipients"
        if failed_recipients:
            message += f". Failed to send to {len(failed_recipients)} recipients"
        
        return DMResponse(
            success=True,
            message=message,
            failed_recipients=failed_recipients if failed_recipients else None
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to send bulk DM: {str(e)}")

@app.get("/sessions")
async def list_sessions(api_key: bool = Depends(verify_api_key)):
    sessions = []
    for session_file in sessions_dir.glob("*_session.json"):
        username = session_file.stem.replace("_session", "")
        sessions.append(username)
    return {"sessions": sessions}

@app.delete("/auth/logout/{session_id}")
async def logout(session_id: str, api_key: bool = Depends(verify_api_key)):
    session_file = get_session_file(session_id)
    if session_file.exists():
        session_file.unlink()
        return {"success": True, "message": f"Session {session_id} deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Session not found")

@app.get("/dm/threads", response_model=ThreadsResponse)
async def get_dm_threads(session_id: str, limit: int = 20, filter: str = "", api_key: bool = Depends(verify_api_key)):
    try:
        print(f"Loading session for: {session_id}")
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        print("Session loaded successfully")
        cl = Client()
        print("Client created")
        cl.set_settings(session_data)
        print("Settings applied")
        
        # Get inbox threads using the correct method with parameters
        try:
            print(f"Calling direct_threads with amount={limit}, selected_filter='{filter}'")
            inbox = cl.direct_threads(amount=limit, selected_filter=filter)
            print(f"direct_threads returned: {type(inbox)} with length: {len(inbox) if inbox else 0}")
            
            if not inbox:
                return ThreadsResponse(
                    success=True,
                    threads=[],
                    message="No threads found or empty inbox"
                )
                
        except Exception as e:
            print(f"Exception in direct_threads: {e}")
            # Handle Pydantic validation errors gracefully
            if "validation error" in str(e).lower() or "model_type" in str(e).lower():
                print("Pydantic validation error detected, trying alternative approach")
                return ThreadsResponse(
                    success=False,
                    threads=[],
                    message="Threads endpoint temporarily unavailable due to Instagram API changes. Use /dm/search/{username}/messages for specific conversations."
                )
            raise HTTPException(status_code=400, detail=f"Error calling direct_threads: {str(e)}")
        
        thread_data = []
        for i, thread in enumerate(inbox):
            print(f"Processing thread {i}: {type(thread)}")
            thread_info = {
                "thread_id": getattr(thread, 'id', f"thread_{i}"),
                "thread_title": getattr(thread, 'thread_title', None),
                "users": [],
                "last_activity": None,
                "unread_count": getattr(thread, 'unread_count', 0),
                "is_group": getattr(thread, 'is_group', False),
                "muted": getattr(thread, 'muted', False)
            }
            
            # Handle users safely
            if hasattr(thread, 'users') and thread.users:
                for user in thread.users:
                    user_info = {
                        "username": getattr(user, 'username', 'unknown'),
                        "full_name": getattr(user, 'full_name', 'Unknown')
                    }
                    thread_info["users"].append(user_info)
            
            # Handle last activity
            if hasattr(thread, 'last_activity_at') and thread.last_activity_at:
                thread_info["last_activity"] = thread.last_activity_at.isoformat()
            
            thread_data.append(thread_info)
        
        return ThreadsResponse(
            success=True,
            threads=thread_data,
            message=f"Retrieved {len(thread_data)} DM threads"
        )
    
    except Exception as e:
        print(f"Main exception: {e}")
        raise HTTPException(status_code=400, detail=f"Failed to get DM threads: {str(e)}")

@app.get("/dm/thread/{thread_id}/messages", response_model=MessagesResponse)
async def get_thread_messages(thread_id: str, session_id: str, limit: int = 20, api_key: bool = Depends(verify_api_key)):
    try:
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        cl = Client()
        cl.set_settings(session_data)
        
        # Re-authenticate if needed
        username = os.getenv("INSTAGRAM_USERNAME")
        password = os.getenv("INSTAGRAM_PASSWORD")
        try:
            cl.login(username, password)
            save_session(cl, username)
        except Exception as e:
            if "challenge_required" not in str(e).lower():
                pass  # Already logged in or other non-critical error
        
        # Get messages from the thread
        messages = cl.direct_messages(thread_id, amount=limit)
        
        message_data = []
        for msg in messages:
            message_info = {
                "message_id": getattr(msg, 'id', None),
                "user_id": str(getattr(msg, 'user_id', 'unknown')),
                "timestamp": msg.timestamp.isoformat() if hasattr(msg, 'timestamp') and msg.timestamp else None,
                "text": getattr(msg, 'text', None),
                "message_type": getattr(msg, 'item_type', 'text'),
                "is_sent_by_viewer": getattr(msg, 'is_sent_by_viewer', False),
                "seen_at": msg.seen_at.isoformat() if hasattr(msg, 'seen_at') and msg.seen_at else None
            }
            message_data.append(message_info)
        
        return MessagesResponse(
            success=True,
            messages=message_data,
            message=f"Retrieved {len(message_data)} messages from thread"
        )
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get thread messages: {str(e)}")

@app.get("/dm/search/{username}/messages", response_model=MessagesResponse)
async def get_user_dm_messages(username: str, session_id: str, limit: int = 20, api_key: bool = Depends(verify_api_key)):
    try:
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        cl = Client()
        cl.set_settings(session_data)
        
        print(f"Searching for DM thread with username: {username}")
        
        # Search for the thread by username
        search_results = cl.direct_search(username)
        print(f"Search returned {len(search_results) if search_results else 0} results")
        
        if not search_results:
            return MessagesResponse(
                success=True,
                messages=[],
                message=f"No DM thread found with user {username}"
            )
        
        # The search returns users, we need to find the thread with this user
        target_user = search_results[0]
        print(f"Found user: {target_user.username}, ID: {target_user.pk}")
        
        # Get the user ID and find the thread
        user_id = target_user.pk
        thread = cl.direct_thread_by_participants([user_id])
        print(f"Found thread type: {type(thread).__name__}")
        
        # Extract messages from thread structure
        messages = []
        if isinstance(thread, dict) and 'thread' in thread and 'items' in thread['thread']:
            messages = thread['thread']['items'][:limit]
        else:
            return MessagesResponse(
                success=False,
                messages=[],
                message="No messages found in thread structure"
            )
        
        print(f"Retrieved {len(messages)} messages")
        
        message_data = []
        for msg in messages:
            # Convert timestamp from microseconds to ISO format
            timestamp = None
            if 'timestamp' in msg and msg['timestamp']:
                from datetime import datetime
                timestamp = datetime.fromtimestamp(msg['timestamp'] / 1000000).isoformat()
            
            message_info = {
                "message_id": msg.get('item_id', None),
                "user_id": str(msg.get('user_id', 'unknown')),
                "timestamp": timestamp,
                "text": msg.get('text', None),
                "message_type": msg.get('item_type', 'text'),
                "is_sent_by_viewer": msg.get('is_sent_by_viewer', False),
            }
            message_data.append(message_info)
        
        return MessagesResponse(
            success=True,
            messages=message_data,
            message=f"Retrieved {len(message_data)} messages from thread with {username}"
        )
    
    except Exception as e:
        print(f"Error in get_user_dm_messages: {e}")
        raise HTTPException(status_code=400, detail=f"Failed to get DM messages for {username}: {str(e)}")

@app.post("/dm/thread/{thread_id}/mark-seen")
async def mark_thread_seen(thread_id: str, session_id: str, api_key: bool = Depends(verify_api_key)):
    try:
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        cl = Client()
        cl.set_settings(session_data)
        
        cl.direct_thread_mark_seen(thread_id)
        
        return {
            "success": True,
            "message": f"Thread {thread_id} marked as seen"
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to mark thread as seen: {str(e)}")

@app.get("/dm/recent-conversations")
async def get_recent_conversations(session_id: str, api_key: bool = Depends(verify_api_key)):
    """
    Alternative to /dm/threads - returns recent conversation info without full thread data
    This endpoint provides a workaround for Pydantic validation issues
    """
    try:
        session_data = load_session(session_id)
        if not session_data:
            raise HTTPException(status_code=401, detail="Session not found. Please login first.")
        
        cl = Client()
        cl.set_settings(session_data)
        
        print("Getting recent conversations using alternative method")
        
        # Try to get basic thread info without full validation
        try:
            # Use a minimal approach that doesn't trigger validation errors
            conversations = []
            
            # This is a placeholder that returns guidance for now
            return {
                "success": True,
                "conversations": [],
                "message": "Use /dm/search/{username}/messages to read messages from specific users",
                "tip": "If you know usernames you've messaged, use the search endpoint directly"
            }
            
        except Exception as e:
            print(f"Error getting conversations: {e}")
            return {
                "success": False,
                "conversations": [],
                "message": f"Could not retrieve conversations: {str(e)}"
            }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to get recent conversations: {str(e)}")

@app.get("/test/threads")
async def test_direct_threads(session_id: str, api_key: bool = Depends(verify_api_key)):
    try:
        session_data = load_session(session_id)
        if not session_data:
            return {"error": "Session not found"}
        
        cl = Client()
        cl.set_settings(session_data)
        
        # Try the most basic call possible
        result = cl.direct_threads(amount=1)
        
        return {
            "success": True,
            "result_type": str(type(result)),
            "result_length": len(result) if result else 0,
            "first_item_type": str(type(result[0])) if result and len(result) > 0 else "none"
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "error_type": str(type(e))
        }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "Instagram DM API",
        "version": "1.0.0",
        "timestamp": os.getenv("TIMESTAMP", "unknown")
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)