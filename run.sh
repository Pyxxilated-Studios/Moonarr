#!/bin/bash

bun index.js || bun index.js &
uvicorn api.main:api --host 0.0.0.0 --port 8000
