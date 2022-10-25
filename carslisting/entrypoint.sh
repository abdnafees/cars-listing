#!/bin/sh

python manage.py makemigrations
python manage.py migrate
echo 'Importing car data'
python manage.py populate_cars
exec "$@"