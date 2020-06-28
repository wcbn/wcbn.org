#!/bin/sh
# entrypoint.sh

set -e

if [ "$DJANGO_SETTINGS_MODULE" == "app.environments.development" ]; then
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 2
done
>&2 echo "Postgres is up"

./manage.py makemigrations
./manage.py migrate
./manage.py collectstatic --noinput
./manage.py runserver 0.0.0.0:8000

else

./manage.py migrate
./manage.py collectstatic --noinput --clear
gunicorn app.wsgi:application --bind 0.0.0.0:$PORT

# restart wsgi
# touch project_name/wsgi.py
fi
