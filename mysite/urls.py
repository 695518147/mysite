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
from xiaobing import views

xversion.register_models()

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('blog/', include('blog.urls')),
    path('xiaobing/', include('xiaobing.urls')),
    path('info/', views.info),
    path('ueditor/', include('djangoUeditor.urls')),
]

handler404 = "error.views.page_not_found"
handler500 = "error.views.service_error"
handler400 = "error.views.service_error"

urlpatterns += [
    # 媒体文件前缀
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # 文件前缀
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
