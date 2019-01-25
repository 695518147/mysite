FROM python:3.7.2

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE mysite.settings

ADD . .

# 依赖安装
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r  plist.txt

#静态文件聚集
RUN  echo yes | python manage.py collectstatic
RUN  python manage.py migrate

EXPOSE 9091:9091


CMD ["python", "manage.py" ,"runserver", "0.0.0.0:9091"]
