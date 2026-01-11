#!/bin/bash

echo "-----> Python version check"
python --version

echo "-----> Upgrading pip (optional but good)"
python -m pip install --upgrade pip

echo "-----> Installing dependencies"
python -m pip install -r requirements.txt

echo "-----> Collecting static files"
python manage.py collectstatic --noinput --clear

python3 manage.py migrate --noinput

python3 manage.py collectstatic --noinput --clear

echo "Build finished!"
