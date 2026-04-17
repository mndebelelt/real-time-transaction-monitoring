#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
REPO_ROOT=$(cd "$SCRIPT_DIR/.." && pwd)

echo "Bootstrapping VM from repo root: $REPO_ROOT"

# Install Docker if missing
if ! command -v docker >/dev/null 2>&1; then
  echo "Installing Docker..."
  sudo apt update
  sudo apt install -y docker.io
fi

# Ensure Docker daemon is running
if ! sudo systemctl is-active --quiet docker; then
  echo "Starting Docker service..."
  sudo systemctl enable --now docker
fi

# Ensure Docker Compose is available
if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
  DOCKER_COMPOSE_CMD="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  DOCKER_COMPOSE_CMD="docker-compose"
else
  echo "Installing Docker Compose plugin..."
  sudo apt install -y docker-compose-plugin
  if docker compose version >/dev/null 2>&1; then
    DOCKER_COMPOSE_CMD="docker compose"
  else
    echo "Installing legacy docker-compose package..."
    sudo apt install -y docker-compose
    DOCKER_COMPOSE_CMD="docker-compose"
  fi
fi

echo "Using compose command: $DOCKER_COMPOSE_CMD"

cd "$REPO_ROOT/docker"
$DOCKER_COMPOSE_CMD up -d

echo "Docker services started. Installing Python dependencies..."
cd "$REPO_ROOT"
pip3 install -r requirements.txt

echo "Bootstrap complete."
echo "Next steps: open one SSH session and run 'python3 -m app.producer.run_producer'"
echo "and in another session run 'python3 -m app.consumer.run_consumer'."
