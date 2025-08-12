# Telegram Message Forwarding Bot

A simple Telegram bot that forwards any message it receives to a specific Telegram group.

## Features

- ✅ Forwards any type of message (text, photos, videos, documents, etc.)
- ✅ Instant forwarding with confirmation
- ✅ Supports all Telegram message types
- ✅ Built-in commands for bot management
- ✅ Error handling and logging
- ✅ Owner-only status commands

## Setup Instructions

### 1. Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Save the bot token (you'll need it later)

### 2. Get Your Target Group ID

1. Add your bot to the target group where you want messages forwarded
2. Make the bot an admin in the group (optional but recommended)
3. Send a message in the group
4. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
5. Look for the `"chat":{"id":-1001234567890}` field - this is your group ID
6. Note: Group IDs are usually negative numbers

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

1. Copy `env_example.txt` to `.env`
2. Edit `.env` with your actual values:

```env
BOT_TOKEN=your_actual_bot_token_here
TARGET_GROUP_ID=-1001234567890
BOT_OWNER_ID=your_telegram_user_id
```

### 5. Run the Bot

#### Option A: Run Locally
```bash
python bot.py
```

#### Option B: Run with Docker (Recommended)

1. **Build and run with Docker Compose:**
   ```bash
   ./docker.sh start
   ```

2. **Or build and run manually:**
   ```bash
   # Build the Docker image
   docker build -t telegram-forward-bot -f docker/Dockerfile .
   
   # Run the container
   docker run -d \
     --name telegram-forward-bot \
     --env-file .env \
     --restart unless-stopped \
     telegram-forward-bot
   ```

3. **View logs:**
   ```bash
   ./docker.sh logs
   # or
   docker logs telegram-forward-bot
   ```

4. **Stop the bot:**
   ```bash
   ./docker.sh stop
   # or
   docker stop telegram-forward-bot
   ```

## Usage

### For Users

1. Start a chat with your bot
2. Send `/start` to see the welcome message
3. Send any message (text, photo, video, etc.)
4. The bot will instantly forward it to the target group
5. You'll receive a confirmation message

### Bot Commands

- `/start` - Welcome message and instructions
- `/help` - Show help and available commands
- `/status` - Bot status (owner only)

### Supported Message Types

- Text messages
- Photos and images
- Videos and animations
- Documents and files
- Voice messages
- Audio files
- Stickers
- GIFs
- Location sharing
- Contact sharing
- And more!

## Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Your bot token from @BotFather | Yes |
| `TARGET_GROUP_ID` | ID of the group to forward messages to | Yes |
| `BOT_OWNER_ID` | Your Telegram user ID (for admin commands) | No |

### Getting Your User ID

1. Send a message to [@userinfobot](https://t.me/userinfobot)
2. It will reply with your user ID

## Security Features

- Bot commands (starting with `/`) are not forwarded
- Messages from the target group are not forwarded back
- Owner-only commands for status checking
- Error handling prevents bot crashes

## Docker Deployment

### Prerequisites

- Docker installed on your system
- Docker Compose (usually comes with Docker Desktop)

### Quick Start with Docker

1. **Navigate to the project directory:**
   ```bash
   cd support-bot
   ```

2. **Create your `.env` file:**
   ```bash
   cp env_example.txt .env
   # Edit .env with your actual values
   ```

3. **Build and run:**
   ```bash
   ./docker.sh start
   ```

4. **Check logs:**
   ```bash
   ./docker.sh logs
   ```

### Docker Commands

| Command | Description |
|---------|-------------|
| `./docker.sh start` | Start the bot in background |
| `./docker.sh stop` | Stop the bot |
| `./docker.sh logs` | View live logs |
| `./docker.sh restart` | Restart the bot |
| `./docker.sh status` | Check container status |
| `./docker.sh build` | Rebuild the Docker image |
| `./docker.sh clean` | Clean up containers and images |

### Docker Benefits

- ✅ **Consistent Environment**: Same setup across different machines
- ✅ **Easy Deployment**: One command to start/stop
- ✅ **Automatic Restart**: Bot restarts if it crashes
- ✅ **Log Management**: Built-in log rotation
- ✅ **Isolation**: Bot runs in its own container
- ✅ **Portability**: Easy to move between servers

## Deployment

### Local Development

```bash
python bot.py
```

### Production Deployment

For production deployment, consider:

1. **Process Manager**: Use `pm2`, `supervisor`, or `systemd`
2. **Environment**: Use proper `.env` file management
3. **Logging**: Configure proper log rotation
4. **Monitoring**: Set up health checks

Example with `pm2`:

```bash
npm install -g pm2
pm2 start bot.py --name telegram-forward-bot --interpreter python3
pm2 save
pm2 startup
```

## Troubleshooting

### Common Issues

1. **Bot not responding**: Check if the bot token is correct
2. **Messages not forwarded**: Verify the target group ID and bot permissions
3. **Permission errors**: Make sure the bot is added to the target group
4. **Import errors**: Install dependencies with `pip install -r requirements.txt`

### Logs

The bot logs all activities. Check the console output for:
- Successful message forwards
- Error messages
- Bot startup status

## Contributing

Feel free to submit issues and enhancement requests!

## Run Commands:

```
pip3 install -r requirements.txt

python3 bot.py


Docker Run Commands: 

./docker.sh start
./docker.sh logs
./docker.sh stop

Docker Build commands:

docker build -t telegram-forward-bot -f docker/Dockerfile .
ocker run -d \
  --name telegram-forward-bot \
  --env-file .env \
  --restart unless-stopped \
  telegram-forward-bot
```