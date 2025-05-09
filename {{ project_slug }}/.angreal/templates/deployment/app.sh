#!/bin/bash

# Application deployment and management script

set -e

ENV=${1:-development}
COMMAND=${2:-start}

# Project directory (parent of this script's directory)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_DIR"

# Load environment variables
if [ -f ".env.$ENV" ]; then
  echo "Loading environment variables from .env.$ENV"
  export $(grep -v '^#' .env.$ENV | xargs)
fi

# Set environment variable for application
export {{environment_prefix}}ENV="$ENV"

case "$COMMAND" in
  start)
    echo "Starting application in $ENV mode..."
    python -m {{package_name}}.app
    ;;
  docker-start)
    echo "Starting Docker containers in $ENV mode..."
    docker-compose -f deployment/docker-compose.yml up -d
    ;;
  docker-stop)
    echo "Stopping Docker containers..."
    docker-compose -f deployment/docker-compose.yml down
    ;;
  docker-build)
    echo "Building Docker images..."
    docker-compose -f deployment/docker-compose.yml build
    ;;
  docker-logs)
    echo "Showing Docker logs..."
    docker-compose -f deployment/docker-compose.yml logs -f
    ;;
  frontend)
    echo "Starting Streamlit frontend..."
    cd frontend && streamlit run app.py
    ;;
  *)
    echo "Usage: $0 [environment] [command]"
    echo ""
    echo "Environments:"
    echo "  development (default)"
    echo "  production"
    echo "  test"
    echo ""
    echo "Commands:"
    echo "  start (default) - Start the application"
    echo "  docker-start    - Start Docker containers"
    echo "  docker-stop     - Stop Docker containers"
    echo "  docker-build    - Build Docker images"
    echo "  docker-logs     - Show Docker logs"
    echo "  frontend        - Start Streamlit frontend"
    exit 1
    ;;
esac
