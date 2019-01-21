#!/usr/bin/env bash
# startup project
#./install.sh
python manage.py collectstatic --noinput &&
python manage.py migrate &&
uwsgi --ini uwsgi.ini
echo "服务启动！   http://localhost:8080/xiaobing/edit/"