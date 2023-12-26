#!/bin/bash

# Run db migrations
python manage.py migrate

# Creating the cache table
python manage.py createcachetable --database cache_db

# Running development server
gunicorn -c gunicorn_config.py django_poc.wsgi -b 0.0.0.0:8011