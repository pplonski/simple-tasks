#!/bin/bash

start_processes() {
    export DATABASE_NAME=tasks_test
    export SERVER_URL=http://127.0.0.1:8011

    PGPASSWORD=1234 psql --host=127.0.0.1 --port=5433 --username=postgres -c "create database $DATABASE_NAME"
    # start server
    cd ../server
    ./manage.py migrate 1>/dev/null
    #./manage.py runserver  & # 1>/dev/null
    #gunicorn server.wsgi --bind 127.0.0.1:8011 --workers 4 --threads 4  1>/dev/null &
    daphne server.asgi:application --bind 127.0.0.1 --port 8011  1>/dev/null &
    SERVER_PID=$!
    # start worker listener
    python worker_listener.py &
    WORKER_LISTENER_PID=$!
    # start redis listener
    python redis_listener.py &
    REDIS_LISTENER_PID=$!
    # start celery worker
    cd -
    cd ../worker
    ls
    celery -A simple_worker worker --loglevel=info -E  & # 1>/dev/null
    WORKER_PID=$!
    # go back and wait till all run
    cd -
    sleep 3
}

kill_processes() {
    kill -9 $WORKER_PID
    kill -9 $SERVER_PID
    kill -9 $WORKER_LISTENER_PID
    kill -9 $REDIS_LISTENER_PID
    sleep 2 # wait till all killed
    PGPASSWORD=1234 psql --host=127.0.0.1 --port=5433 --username=postgres -c "drop database $DATABASE_NAME"
    unset DATABASE_NAME
}


# testing
start_processes
python run.py
kill_processes
