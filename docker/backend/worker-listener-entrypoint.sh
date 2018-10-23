#!/usr/bin/env bash

cd /app/backend/worker

celery -A simple_worker worker --loglevel=info -E
