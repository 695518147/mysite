# 自定义应用url
from django.urls import path
from xiaobing import views

urlpatterns = [
    path('', views.index),
    path('edit/', views.edit),
    path('saveOrder/', views.saveOrder),
    path('saveType/', views.saveType),
    path('getAllOrderType/', views.getAllOrderType),
    path('getAllOrderByTypeId/', views.getAllOrderByTypeId),
    path('getOrderById/', views.getOrderById),
    path('test1/', views.TestUEditor),
    path('test2/', views.TestUEditorModel),
]
