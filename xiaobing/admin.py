from django.contrib import admin
from xiaobing import models
import xadmin


# Register your models here.
# 格式化列表显示
class OrderPostAdmin(admin.ModelAdmin):
    list_display = ('orderName', 'createTime', 'number')


class OrderTypePostAdmin(admin.ModelAdmin):
    list_display = ('typeName', 'createTime', 'number')


class OrderPostAdmin1(object):
    list_display = ('orderName', 'createTime', 'number')


class OrderTypePostAdmin1(object):
    list_display = ('typeName', 'createTime', 'number')


# Register your models here.     注册所创建的模型   用于admin界面的显示
admin.site.register(models.Order, OrderPostAdmin)
admin.site.register(models.OrderType, OrderTypePostAdmin)

xadmin.site.register(models.Order, OrderPostAdmin1)
xadmin.site.register(models.OrderType, OrderTypePostAdmin1)
