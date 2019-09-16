#!/usr/bin/env bash
set -ex

./manage.py collectstatic --noinput
./manage.py migrate --noinput

# For debugging
#./manage.py runserver 0.0.0.0:8000
gunicorn $USWGI_APP --bind 0.0.0.0:8000 --workers 2 --timeout 300