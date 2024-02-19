#!/bin/sh
set -e

echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

echo "Making migrations and migrating the database. Please wait..."
python manage.py makemigrations
python manage.py migrate

# Start the Django app
exec "$@"
