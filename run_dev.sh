#!/bin/sh

docker compose down -v

sudo rm -rf db

docker compose build

docker compose up -d --remove-orphans