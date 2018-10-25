#!/bin/bash

./node_modules/loadtest/bin/loadtest.js -n 100 -c 10 http://127.0.0.1:8000/api/tasks --data '{"status":"a", "progress":1, "params":"3"}' -m POST -T application/json

