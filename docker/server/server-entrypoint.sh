#!/usr/bin/env bash

cd /app/backend/server
./manage.py migrate

#./manage.py runserver 0.0.0.0:8000 # --settings=djangoreactredux.settings.dev_docker

gunicorn server.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4
