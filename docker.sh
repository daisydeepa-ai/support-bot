#!/bin/bash

# Wrapper script to run Docker commands from the docker folder

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCKER_DIR="$SCRIPT_DIR/docker"

# Check if docker directory exists
if [ ! -d "$DOCKER_DIR" ]; then
    echo "Error: Docker directory not found at $DOCKER_DIR"
    exit 1
fi

# Change to docker directory and run the command
cd "$DOCKER_DIR"
./docker-run.sh "$@" 