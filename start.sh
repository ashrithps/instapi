#!/bin/bash

# Production startup script for Instagram DM API

echo "Starting Instagram DM API..."

# Create sessions directory if it doesn't exist
mkdir -p /app/sessions

# Set proper permissions
chmod 755 /app/sessions

# Start the application with Gunicorn for production
if [ "$ENVIRONMENT" = "production" ]; then
    echo "Starting in production mode with Gunicorn..."
    exec gunicorn main:app \
        --bind 0.0.0.0:${API_PORT:-8000} \
        --workers 2 \
        --worker-class uvicorn.workers.UvicornWorker \
        --timeout 300 \
        --keep-alive 2 \
        --max-requests 1000 \
        --max-requests-jitter 50 \
        --log-level info \
        --access-logfile - \
        --error-logfile -
else
    echo "Starting in development mode with Uvicorn..."
    exec python main.py
fi