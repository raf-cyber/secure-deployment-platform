#!/bin/bash
set -e

echo "Deploying version $VERSION"

docker compose up --build -d

sleep 5

python health_check.py || {
  echo "Deployment failed. Rolling back."
  export VERSION=1.0.0
  docker compose up --build -d
  exit 1
}

echo "Deployment successful"