#!/usr/bin/env bash

cd /app/backend/server
#./manage.py migrate

#./manage.py runserver 0.0.0.0:8000 # --settings=djangoreactredux.settings.dev_docker


daphne server.asgi:application --bind 0.0.0.0 --port 9000
