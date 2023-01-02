#!/bin/bash

pyfiglet SECFI
pyfiglet BACKEND ASSESSMENT CHALLENGE

gunicorn --bind 0.0.0.0:8000 --timeout 600 --workers 4 config.wsgi
