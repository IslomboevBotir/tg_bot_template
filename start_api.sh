#!/bin/sh
# Start Uvicorn processes
echo "Starting Uvicorn."

# Running Uvicorn server
exec uvicorn src.infrastructure.api.app:create_app --host 0.0.0.0 --port "${FASTAPI_PORT:-8000}" --workers 1 --proxy-headers --factory
