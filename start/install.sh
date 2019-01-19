#!/usr/bin/env bash

pip install --upgrade pip
pip install -r plist.txt
pip install uwsgi
../manage.py collectstatic



