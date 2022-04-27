#!/bin/bash
poetry run gunicorn -b :5000 --access-logfile - --error-logfile - ml_app:app
