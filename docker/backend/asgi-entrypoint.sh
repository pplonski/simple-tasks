#!/usr/bin/env bash


until cd /app/backend/server
do
    echo "Waiting for server volume..."
done

until ./manage.py migrate
do
    echo "Waiting for postgres ready..."
    sleep 2
done


daphne server.asgi:application --bind 0.0.0.0 --port 9000
