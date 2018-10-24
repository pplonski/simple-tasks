#!/usr/bin/env bash

until cd /app/backend/server
do
    echo "Waiting for server volume..."
done

python worker_listener.py
