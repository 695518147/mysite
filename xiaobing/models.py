from django.db import models
from django import forms
from djangoUeditor.models import UEditorField
from djangoUeditor.commands import *


# Create your models here.
class Order(models.Model):
    typeId = models.CharField(max_length=100, null=True, blank=True)
    isShow = models.CharField(u'是否显示指令说明', max_length=10, null=True, blank=True)
    isShowOrder = models.CharField(u'是否显示该条指令', max_length=10, null=True, blank=True)
    orderId = models.CharField(max_length=100, null=True, blank=True)
    orderName = UEditorField(u'指令名称', blank=True, toolbars="mini", imagePath="image/order", settings={"a": 1})
    orderDescription = UEditorField(u'指令说明', default='test', imagePath="image/order", toolbars="mini")
    typeDescription = UEditorField(u'类型说明', toolbars="mini", default='test', imagePath="image/order")

    createTime = models.DateTimeField(u'创建时间')
    number = models.IntegerField(u'排序', default=99)

    class Meta:
        ordering = ("-createTime",)


class OrderType(models.Model):
    typeId = models.CharField(max_length=100, null=True, blank=True)
    typeName = UEditorField(u'类型名称', toolbars="mini", imagePath="image/orderType")
    createTime = models.DateTimeField(u'创建时间')
    number = models.IntegerField(u'排序', default=99)

    class Meta:
        ordering = ("number", "-createTime",)
