#coding:utf-8
from djangoUeditor.views import get_ueditor_controller
from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = [
    path("controller/", get_ueditor_controller),
]
