#!/usr/bin/env bash

DOCKER_BUILDKIT=1 docker buildx build \
  -t fantasy-football-catalog:latest \
  .