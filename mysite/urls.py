"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

import xadmin
from mysite import settings
from django.views.static import serve

from xadmin.plugins import xversion
from xiaobing import views


admin.autodiscover()
xadmin.autodiscover()
xversion.register_models()

from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('blog/', include('blog.urls')),
    path('', views.index),
    path('xiaobing/', include('xiaobing.urls')),
    path('ueditor/', include('djangoUeditor.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        # 媒体文件前缀
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        # 文件前缀
        re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
        re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
        ]
