#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@gmail.com"}
cd /app/

#/opt/venv/bin/python manage.py migrate --noinput

/opt/venv/bin/python manage.py makemigrations app --noinput
/opt/venv/bin/python manage.py migrate app --noinput
/opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
