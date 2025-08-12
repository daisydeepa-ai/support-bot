#!/bin/bash

# Telegram Bot Docker Management Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

# Check if .env file exists
check_env() {
    if [ ! -f "../.env" ]; then
        print_error ".env file not found!"
        print_status "Creating .env from template..."
        if [ -f "../env_example.txt" ]; then
            cp ../env_example.txt ../.env
            print_warning "Please edit .env file with your actual values before running the bot!"
            exit 1
        else
            print_error "env_example.txt not found either!"
            exit 1
        fi
    fi
}

# Function to show usage
show_usage() {
    echo "Usage: $0 {start|stop|restart|logs|status|build|clean}"
    echo ""
    echo "Commands:"
    echo "  start   - Start the bot with docker-compose"
    echo "  stop    - Stop the bot"
    echo "  restart - Restart the bot"
    echo "  logs    - Show bot logs"
    echo "  status  - Show container status"
    echo "  build   - Build the Docker image"
    echo "  clean   - Remove containers and images"
    echo ""
}

# Function to start the bot
start_bot() {
    print_header "Starting Telegram Bot"
    check_env
    print_status "Starting bot with docker-compose..."
    docker-compose -f docker-compose.yml up -d
    print_status "Bot started successfully!"
    print_status "Use '$0 logs' to view logs"
}

# Function to stop the bot
stop_bot() {
    print_header "Stopping Telegram Bot"
    print_status "Stopping bot..."
    docker-compose -f docker-compose.yml down
    print_status "Bot stopped successfully!"
}

# Function to restart the bot
restart_bot() {
    print_header "Restarting Telegram Bot"
    print_status "Restarting bot..."
    docker-compose -f docker-compose.yml restart
    print_status "Bot restarted successfully!"
}

# Function to show logs
show_logs() {
    print_header "Bot Logs"
    print_status "Showing logs (Ctrl+C to exit)..."
    docker-compose -f docker-compose.yml logs -f
}

# Function to show status
show_status() {
    print_header "Container Status"
    docker-compose -f docker-compose.yml ps
}

# Function to build the image
build_image() {
    print_header "Building Docker Image"
    print_status "Building image..."
    docker-compose -f docker-compose.yml build
    print_status "Image built successfully!"
}

# Function to clean up
clean_up() {
    print_header "Cleaning Up"
    print_warning "This will remove all containers and images!"
    read -p "Are you sure? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        print_status "Stopping containers..."
        docker-compose -f docker-compose.yml down
        print_status "Removing images..."
        docker rmi telegram-forward-bot 2>/dev/null || true
        print_status "Cleanup completed!"
    else
        print_status "Cleanup cancelled."
    fi
}

# Main script logic
case "$1" in
    start)
        start_bot
        ;;
    stop)
        stop_bot
        ;;
    restart)
        restart_bot
        ;;
    logs)
        show_logs
        ;;
    status)
        show_status
        ;;
    build)
        build_image
        ;;
    clean)
        clean_up
        ;;
    *)
        show_usage
        exit 1
        ;;
esac 