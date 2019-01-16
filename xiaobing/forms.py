# coding:utf-8
from django import forms
from xiaobing.models import Order


class OrderForm(forms.Form):
    class Meta:
        model = Order
        exclude = ('timestamp',)