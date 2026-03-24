#!/bin/bash

# Simple deployment script example for cloud app

APP_NAME="my-cloud-app"
DOCKER_IMAGE="myrepo/my-cloud-app:latest"

function deploy() {
  echo "Building Docker image $DOCKER_IMAGE..."
  docker build -t $DOCKER_IMAGE . || { echo "Docker build failed"; exit 1; }

  echo "Pushing Docker image to repository..."
  docker push $DOCKER_IMAGE || { echo "Docker push failed"; exit 1; }

  echo "Deploying to cloud via kubectl..."
  kubectl set image deployment/$APP_NAME $APP_NAME=$DOCKER_IMAGE --record || { echo "Deploy failed"; exit 1; }

  echo "Deployment started, check pod status with kubectl get pods"
}

deploy
