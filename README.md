# Instagram DM API

A FastAPI-based service for sending Instagram Direct Messages using the instagrapi library.

## Features

- Instagram authentication with session persistence
- Send DM to individual users
- Send bulk DMs to multiple users
- Session management
- Error handling and validation

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy environment file and configure:
```bash
cp .env.example .env
```

3. Run the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication

#### POST `/auth/login`
Login to Instagram and save session
```json
{
  "username": "your_username",
  "password": "your_password",
  "verification_code": "123456"  // Optional: for 2FA enabled accounts
}
```

**2FA Support:**
- If your account has 2FA enabled, first call without `verification_code`
- The API will respond with `requires_2fa: true`
- Get the verification code from your authenticator app
- Call the endpoint again with the `verification_code`

#### DELETE `/auth/logout/{session_id}`
Delete a saved session

#### GET `/sessions`
List all saved sessions

### Direct Messages

#### POST `/dm/send?session_id={session_id}`
Send DM to a single user
```json
{
  "recipient_username": "target_username",
  "message": "Hello from the API!"
}
```

#### POST `/dm/send-bulk?session_id={session_id}`
Send DM to multiple users
```json
{
  "recipient_usernames": ["user1", "user2", "user3"],
  "message": "Hello everyone!"
}
```

### Reading Messages

#### GET `/dm/threads?session_id={session_id}&limit=20`
Get list of DM threads/conversations
- `limit`: Number of threads to retrieve (default: 20)

Returns thread information including:
- Thread ID, title, participants
- Last activity, unread count
- Group status, muted status

#### GET `/dm/thread/{thread_id}/messages?session_id={session_id}&limit=20`
Get messages from a specific thread
- `thread_id`: ID of the thread to read
- `limit`: Number of messages to retrieve (default: 20)

Returns message details including:
- Message content, timestamp, sender
- Message type, seen status

#### POST `/dm/thread/{thread_id}/mark-seen?session_id={session_id}`
Mark a thread as seen/read

## Usage Example

**Important**: All endpoints require an API key in the `X-API-Key` header.

1. First, authenticate (without 2FA):
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_secure_api_key_here" \
  -d '{"verification_code": ""}'
```

1b. If 2FA is required, authenticate with verification code:
```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_secure_api_key_here" \
  -d '{"verification_code": "123456"}'
```

2. Send a DM:
```bash
curl -X POST "http://localhost:8000/dm/send?session_id=your_username" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_secure_api_key_here" \
  -d '{"recipient_username": "target_user", "message": "Hello!"}'
```

3. Read DM threads:
```bash
curl -X GET "http://localhost:8000/dm/threads?session_id=your_username&limit=10" \
  -H "X-API-Key: your_secure_api_key_here"
```

4. Read messages from a specific thread:
```bash
curl -X GET "http://localhost:8000/dm/thread/THREAD_ID/messages?session_id=your_username&limit=20" \
  -H "X-API-Key: your_secure_api_key_here"
```

5. Mark thread as seen:
```bash
curl -X POST "http://localhost:8000/dm/thread/THREAD_ID/mark-seen?session_id=your_username" \
  -H "X-API-Key: your_secure_api_key_here"
```

## Security Notes

- Sessions are stored locally in the `sessions/` directory
- Never commit your `.env` file with real credentials
- Use strong passwords and enable 2FA on your Instagram account
- Be mindful of Instagram's rate limits and terms of service

## Interactive API Documentation

Visit `http://localhost:8000/docs` for Swagger UI documentation.