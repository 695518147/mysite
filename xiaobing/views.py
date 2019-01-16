from django.core import serializers
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from xiaobing.models import Order, OrderType
from xiaobing.forms import OrderForm
from pypinyin import pinyin, Style


# Create your views here.pip

def index(request):
    return render(request, "index.html")


def edit(request):
    orders = Order.objects.all()[:10]
    return render(request, "add.html", {"orders": orders})


def saveOrder(request):
    if "POST" == request.method:
        typeId = request.POST['typeId']
        isShow = request.POST['isShow']
        isShowOrder = request.POST['isShowOrder']
        orderName = request.POST['orderName']
        orderNameText = request.POST['orderNameText']
        pyls = pinyin(orderNameText, style=Style.FIRST_LETTER)
        orderId = ""
        for py in pyls:
            orderId = orderId + str(py[0])
        number = request.POST['number']
        orderDescription = request.POST['orderDescription']
        typeDescription = request.POST['typeDescription']

        Order.objects.create(typeId=typeId, isShowOrder=isShowOrder, orderId=orderId, isShow=isShow,
                             orderName=orderName,
                             orderDescription=orderDescription,
                             typeDescription=typeDescription, number=number, createTime=datetime.now())
    return HttpResponseRedirect("../edit/")


def saveType(request):
    if "POST" == request.method:
        typeName = request.POST['typeName']
        typeNameText = request.POST['typeNameText']
        number = request.POST['number']
        pyls = pinyin(typeNameText, style=Style.FIRST_LETTER)
        typeId = ""
        for py in pyls:
            typeId = typeId + str(py[0])
        OrderType.objects.create(typeId=typeId, typeName=typeName, number=number, createTime=datetime.now())
    orders = OrderType.objects.all()
    return HttpResponse(serializers.serialize("json", orders))


# 获取所有指令类型
def getAllOrderType(request):
    orderTypes = OrderType.objects.all().order_by('number')
    return HttpResponse(serializers.serialize("json", orderTypes))


# 根据指令类型ID获取指令集合
def getAllOrderByTypeId(request):
    typeId = request.GET['typeId']
    orders = Order.objects.filter(typeId=typeId, isShowOrder="true").order_by('number')
    return HttpResponse(serializers.serialize("json", orders))


# 根据id获取order
def getOrderById(request):
    orderId = request.GET['orderId']
    order = Order.objects.filter(orderId=orderId).order_by('number')
    return HttpResponse(serializers.serialize('json', order))


def TestUEditor(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
    else:
        form = OrderForm(
            initial={'orderName': u'测试'}
        )

    return render(request, 'test2.html', {'form': form})


def TestUEditorModel(request):
    if request.method == 'POST':
        # M=Blog.objects.get(pk=1)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'test.html', {'form': form})
        else:
            return HttpResponse(u"数据校验错误")
    else:
        try:
            M = Order.objects.get(pk=1)
            form = OrderForm(instance=M)
        except:
            form = OrderForm(
                initial={'orderName': '测试'}
            )
        return render(request, 'test.html', {'form': form})
