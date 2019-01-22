### 项目启动会流程

- python版本  
    3以上
    
- 数据库配置  

```
    修改mysite文件中的DATABASES的相关配置。
```

- 基础数据与表的创建

    执行外层mysite目录下的mange.py文件
```
python manage.py makemigrations
python manage.py migrate
```

- 服务启动前准备

```
    1.启动mysql服务
    2.静态文件同意处理执行：python manage.py collectstatic
    3.创建超级用户：python manage.py createsuperuser
``` 

- 两种启动服务

```
    1.使用uwsgi：
        启动：start.sh
        停止：stop.sh
       
     2.直接使用manage.py
        python manage.py runserver 8088 --insecure
    
```

