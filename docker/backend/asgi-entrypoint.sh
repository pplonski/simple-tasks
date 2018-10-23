#!/usr/bin/env bash

cd /app/backend/server
./manage.py migrate

daphne server.asgi:application --bind 0.0.0.0 --port 9000
