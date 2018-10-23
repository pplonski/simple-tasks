#!/usr/bin/env bash

cd /app/backend/server
./manage.py migrate

gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4

#./manage.py runserver 0.0.0.0:8000 # --settings=djangoreactredux.settings.dev_docker
