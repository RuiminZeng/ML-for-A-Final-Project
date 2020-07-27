#!/usr/bin/env bash
# This tags and uploads an image to Docker Hub

#Assumes flasksklearn is built

dockerpath="yujiechen99/flasksklearn"

# Authenticate & Tag
echo "Docker ID and Image: $dockerpath"
docker login &&\
    docker image tag flasksklearn $dockerpath

# Push Image
docker image push $dockerpath