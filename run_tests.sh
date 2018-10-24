#!/bin/bash

sudo docker-compose up --build -d
sleep 3
python backend/tests/run.py

sudo docker-compose down
