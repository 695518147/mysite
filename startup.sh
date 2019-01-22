#!/usr/bin/env bash
# startup project
#./install.sh
python echo yes | manage.py collectstatic
python manage.py migrate &&
uwsgi --ini uwsgi.ini
echo "服务启动"