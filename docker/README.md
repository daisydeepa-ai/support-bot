# Docker Configuration

This folder contains all Docker-related files for the Telegram Forward Bot.

## 📁 Contents

- **`Dockerfile`** - Docker image definition
- **`docker-compose.yml`** - Docker Compose configuration
- **`.dockerignore`** - Files to exclude from Docker build
- **`docker-run.sh`** - Management script for Docker operations
- **`DOCKER_GUIDE.md`** - Comprehensive Docker documentation

## 🚀 Quick Start

### From the main project directory (recommended):
```bash
cd support-bot
./docker.sh start
```

### From this directory:
```bash
cd support-bot/docker
./docker-run.sh start
```

## 📖 Documentation

For detailed Docker instructions, see:
- **`DOCKER_GUIDE.md`** - Complete Docker guide
- **`../README.md`** - Main project documentation

## 🔧 Management

Use the wrapper script from the main directory:
```bash
./docker.sh {start|stop|restart|logs|status|build|clean}
```

Or use the management script from this directory:
```bash
./docker-run.sh {start|stop|restart|logs|status|build|clean}
``` 