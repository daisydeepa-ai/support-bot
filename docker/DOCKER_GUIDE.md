# Docker Guide for Telegram Forward Bot

This guide explains how to deploy and manage the Telegram Forward Bot using Docker.

## 📁 Project Structure

```
support-bot/
├── bot.py                 # Main bot application
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables template
├── docker.sh              # Docker wrapper script
├── docker/                # Docker configuration folder
│   ├── Dockerfile         # Docker image definition
│   ├── docker-compose.yml # Docker Compose configuration
│   ├── .dockerignore      # Files to exclude from Docker build
│   ├── docker-run.sh      # Management script
│   └── DOCKER_GUIDE.md    # This documentation
└── README.md              # Project documentation
```

## 🚀 Quick Start

### Prerequisites

- Docker installed on your system
- Docker Compose (usually comes with Docker Desktop)

### Step 1: Setup Environment

```bash
cd support-bot
cp env_example.txt .env
# Edit .env with your actual values
```

### Step 2: Start the Bot

```bash
# Using the wrapper script (recommended)
cd support-bot
./docker.sh start

# Or using the management script directly
cd support-bot/docker
./docker-run.sh start

# Or using docker-compose directly
cd support-bot/docker
docker-compose up -d
```

### Step 3: Check Status

```bash
# From support-bot directory
./docker.sh status

# From docker directory
./docker-run.sh status
# or
docker-compose ps
```

## 🛠️ Management Commands

### Using the Wrapper Script (Recommended)

```bash
# From support-bot directory
./docker.sh start    # Start the bot
./docker.sh stop     # Stop the bot
./docker.sh restart  # Restart the bot
./docker.sh logs     # View logs
./docker.sh status   # Check status
./docker.sh build    # Rebuild image
./docker.sh clean    # Clean up containers/images
```

### Using the Management Script Directly

```bash
# From docker directory
./docker-run.sh start    # Start the bot
./docker-run.sh stop     # Stop the bot
./docker-run.sh restart  # Restart the bot
./docker-run.sh logs     # View logs
./docker-run.sh status   # Check status
./docker-run.sh build    # Rebuild image
./docker-run.sh clean    # Clean up containers/images
```

### Using Docker Compose Directly

```bash
docker-compose up -d      # Start in background
docker-compose down       # Stop and remove containers
docker-compose restart    # Restart services
docker-compose logs -f    # Follow logs
docker-compose ps         # Show status
docker-compose build      # Build images
```

## 🔧 Configuration

### Environment Variables

The bot uses these environment variables (set in `.env` file):

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram bot token from @BotFather | Yes |
| `TARGET_GROUP_ID` | ID of the target group | Yes |
| `BOT_OWNER_ID` | Your Telegram user ID | No |

### Docker Configuration

The `docker-compose.yml` includes:

- **Auto-restart**: Container restarts if it crashes
- **Log rotation**: Logs are limited to 10MB with 3 files
- **Health checks**: Container health is monitored
- **Volume mounting**: Logs are persisted to host
- **Network isolation**: Bot runs in its own network

## 📊 Monitoring

### View Logs

```bash
# Follow logs in real-time
./docker-run.sh logs

# View last 100 lines
docker-compose logs --tail=100

# View logs for specific service
docker-compose logs telegram-bot
```

### Check Status

```bash
# Container status
./docker-run.sh status

# Resource usage
docker stats telegram-forward-bot

# Health check
docker inspect telegram-forward-bot | grep Health -A 10
```

## 🔄 Updates

### Update Bot Code

1. **Stop the bot:**
   ```bash
   ./docker-run.sh stop
   ```

2. **Rebuild the image:**
   ```bash
   ./docker-run.sh build
   ```

3. **Start the bot:**
   ```bash
   ./docker-run.sh start
   ```

### Update Dependencies

1. **Modify `requirements.txt`**
2. **Rebuild the image:**
   ```bash
   ./docker-run.sh build
   ```
3. **Restart the bot:**
   ```bash
   ./docker-run.sh restart
   ```

## 🧹 Maintenance

### Clean Up

```bash
# Remove containers and images
./docker-run.sh clean

# Remove unused Docker resources
docker system prune -f

# Remove all unused images
docker image prune -a
```

### Backup

```bash
# Backup logs
tar -czf bot-logs-$(date +%Y%m%d).tar.gz logs/

# Backup configuration
cp .env .env.backup
```

## 🐛 Troubleshooting

### Common Issues

1. **Container won't start:**
   ```bash
   docker-compose logs
   # Check for missing .env file or invalid values
   ```

2. **Bot not responding:**
   ```bash
   ./docker-run.sh logs
   # Check for bot token or group ID issues
   ```

3. **Permission errors:**
   ```bash
   chmod +x docker-run.sh
   ```

4. **Port conflicts:**
   - The bot doesn't use any ports, so this shouldn't be an issue

### Debug Mode

```bash
# Run in foreground to see logs
docker-compose up

# Run with shell access
docker-compose run --rm telegram-bot /bin/bash
```

## 🔒 Security

### Best Practices

- ✅ **Non-root user**: Container runs as `appuser`
- ✅ **Environment isolation**: Variables in `.env` file
- ✅ **Network isolation**: Bot runs in dedicated network
- ✅ **Log rotation**: Prevents disk space issues
- ✅ **Health checks**: Monitors container health

### Production Deployment

For production, consider:

1. **Use Docker secrets** for sensitive data
2. **Set up monitoring** (Prometheus, Grafana)
3. **Configure log aggregation** (ELK stack)
4. **Use Docker Swarm or Kubernetes** for orchestration
5. **Set up automated backups**

## 📈 Performance

### Resource Usage

Typical resource usage:
- **CPU**: 1-5% (idle)
- **Memory**: 50-100MB
- **Disk**: 200-500MB (including image)

### Optimization

- **Multi-stage builds** for smaller images
- **Alpine Linux** base for minimal size
- **Layer caching** for faster builds
- **Resource limits** in production

## 🤝 Contributing

When contributing to the Docker setup:

1. **Test locally** before submitting
2. **Update documentation** for new features
3. **Follow Docker best practices**
4. **Include health checks** for new services
5. **Update the management script** if needed 