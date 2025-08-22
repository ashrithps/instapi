# Deployment Guide for Instagram DM API

## Dokploy Deployment

### Prerequisites
- Dokploy instance running
- Git repository access
- Instagram account credentials

### Deployment Steps

1. **Push your code to a Git repository** (GitHub, GitLab, etc.)

2. **Create a new application in Dokploy:**
   - Go to your Dokploy dashboard
   - Click "Create Application"
   - Choose "Docker" as the application type
   - Connect your Git repository

3. **Set Environment Variables in Dokploy:**
   ```
   INSTAGRAM_USERNAME=your_instagram_username
   INSTAGRAM_PASSWORD=your_instagram_password
   SESSION_FILE_PATH=/app/sessions/
   API_PORT=8000
   APP_API_KEY=your_secure_api_key_here
   ENVIRONMENT=production
   ```

4. **Configure the deployment:**
   - Build context: `/`
   - Dockerfile path: `Dockerfile`
   - Port mapping: `8000:8000`

5. **Deploy the application:**
   - Click "Deploy"
   - Wait for the build and deployment to complete

### Health Check
The application includes a health check endpoint at `/health` that Dokploy can use to monitor the service.

### Volume Persistence
For session persistence across deployments, configure a volume mount:
- Mount path: `/app/sessions`
- This will preserve Instagram login sessions between container restarts

### Security Considerations
- Never commit the `.env` file with real credentials
- Use Dokploy's environment variable management
- Consider using secrets management for production
- Enable HTTPS in Dokploy for secure API access

### Scaling
The application is configured with Gunicorn for production:
- 2 worker processes by default
- Can handle multiple concurrent requests
- Adjust workers in `start.sh` based on your server resources

### Monitoring
- Health check endpoint: `GET /health`
- Application logs available in Dokploy dashboard
- Monitor Instagram API rate limits

### Troubleshooting
1. **Build failures**: Check that all dependencies in `requirements.txt` are correct
2. **Runtime errors**: Check environment variables are set correctly
3. **Instagram login issues**: Verify credentials and handle 2FA properly
4. **Session persistence**: Ensure volume mount is configured correctly

## Local Testing with Docker

Test the deployment locally before pushing to Dokploy:

```bash
# Build the image
docker build -t instapi .

# Run with environment variables
docker run -p 8000:8000 \
  -e INSTAGRAM_USERNAME=your_username \
  -e INSTAGRAM_PASSWORD=your_password \
  -e ENVIRONMENT=production \
  instapi

# Or use docker-compose
docker-compose up
```

## API Usage After Deployment

Once deployed, your API will be available at your Dokploy domain:

```bash
# Health check
curl https://your-domain.com/health

# Login (with 2FA if needed)
curl -X POST "https://your-domain.com/auth/login" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_secure_api_key_here" \
  -d '{"verification_code": "123456"}'

# Send DM
curl -X POST "https://your-domain.com/dm/send?session_id=username" \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_secure_api_key_here" \
  -d '{"recipient_username": "target", "message": "Hello!"}'
```