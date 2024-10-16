#!/bin/bash

echo "Waiting for MongoDB and Redis..."

while ! nc -z $MONGO_HOST $MONGO_PORT; do
  echo "Waiting for MongoDB..."
  sleep 5
done

while ! nc -z $REDIS_HOST $REDIS_PORT; do
  echo "Waiting for Redis..."
  sleep 5
done

echo "MongoDB and Redis are up, starting the server..."

# Run migrations and collect static files
python manage.py migrate
python manage.py collectstatic --noinput

# Start the Daphne server as the main process
exec daphne -b 0.0.0.0 -p 8000 chatproject.asgi:application
