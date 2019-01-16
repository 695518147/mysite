from django.contrib import admin
from blog import models


# 格式化列表显示
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


# Register your models here.     注册所创建的模型   用于admin界面的显示
admin.site.register(models.BlogPost, BlogPostAdmin)
