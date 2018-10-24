#!/usr/bin/env bash

until cd /app/backend/worker
do
    echo "Waiting for worker volume..."
done

python worker_listener.py
