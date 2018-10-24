#!/usr/bin/env bash

until cd /app/backend/worker
do
    echo "Waiting for worker volume..."
done

celery -A simple_worker worker --loglevel=info -E
