#!/bin/bash
docker build -t flaskapp:1.0 .
docker run -d --name redis redis:alpine
docker run --link redis:redis -p 5000:5000 flaskapp:1.0
