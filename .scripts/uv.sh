#!/usr/bin/env bash

SCRIPT_PATH=${0%/*}

docker compose run --rm bash

_exit_code=$?

if [ $_exit_code -eq 0 ]; then
  "$SCRIPT_PATH"/docker-build.sh
fi
