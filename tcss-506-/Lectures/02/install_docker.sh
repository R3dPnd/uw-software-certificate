#!/bin/bash

# Script to install Docker on Ubuntu 24.04
# This script installs Docker Engine, containerd, and Docker Compose
#
# Usage: ./install_docker.sh
# Run with sudo or as root

# Stop script execution on any error
set -e

echo "=== Docker Installation Script for Ubuntu 24.04 ==="

# Check if running as root or with sudo
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script with sudo or as root"
  exit 1
fi

# Check if system is Ubuntu 24.04
if ! grep -q "Ubuntu 24.04" /etc/os-release; then
  echo "This script is designed for Ubuntu 24.04"
  echo "Your system: $(grep "PRETTY_NAME" /etc/os-release | cut -d= -f2 | tr -d \")"
  read -p "Continue anyway? (y/n): " choice
  if [[ ! "$choice" =~ ^[Yy]$ ]]; then
    exit 1
  fi
fi

echo "=== Updating package information ==="
apt update

echo "=== Installing required dependencies ==="
apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

echo "=== Adding Docker's official GPG key ==="
# Create directory for keyrings if it doesn't exist
mkdir -p /etc/apt/keyrings
# Download and add GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
  gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo "=== Setting up Docker repository ==="
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "=== Updating package information with Docker repository ==="
apt update

echo "=== Installing Docker Engine, containerd, and Docker Compose ==="
apt install -y \
  docker-ce \
  docker-ce-cli \
  containerd.io \
  docker-compose-plugin \
  docker-buildx-plugin

echo "=== Adding ubuntu user to the docker group ==="
# Set username to ubuntu
USER_TO_ADD="ubuntu"

# Check if the ubuntu user exists
if id "$USER_TO_ADD" &>/dev/null; then
  usermod -aG docker "$USER_TO_ADD"
  echo "Added $USER_TO_ADD to the docker group"
  echo "NOTE: User $USER_TO_ADD needs to log out and log back in for this to take effect"
else
  echo "Warning: User $USER_TO_ADD does not exist. Docker group not assigned to any user."
fi

echo "=== Verifying Docker installation ==="
# Check Docker version
docker --version
# Check Docker Compose version
docker compose version
# Run hello-world container to verify installation
docker run --rm hello-world

echo "=== Docker has been successfully installed! ==="
echo "You can start using Docker now. If you added your user to the docker group,"
echo "remember to log out and log back in to apply the changes."