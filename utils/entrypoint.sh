#!/bin/sh
set -e
pwd
ls
python manage.py shell < /wait-for-mysql.py
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
