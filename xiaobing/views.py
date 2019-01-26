from django.core import serializers
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import djangoUeditor.settings as USettings
from xiaobing.models import Order, OrderType
from xiaobing.forms import OrderForm
from pypinyin import pinyin, Style
from django.db.models import Q
from xiaobing.json import DateEncoder
import json
import jieba
import re
import os
from urllib import parse
from django.contrib.auth.decorators import login_required


# Create your views here.pip

def index(request):
    return render(request, "index.html")


def info(request):
    string = request._current_scheme_host
    return HttpResponse("Successful start-up of the service at address " + string)


def deleteFile(request):
    paths = request.POST.get("paths")
    path = json.loads(paths)

    for p in path:
        pa = p.replace(USettings.gSettings.MEDIA_URL, "")
        OutputPath = os.path.join(USettings.gSettings.MEDIA_ROOT, pa)
        filepath = parse.unquote(OutputPath)
        print(filepath)
        if os.path.exists(filepath):
            os.remove(filepath)
            return HttpResponse('ok')


def deleteOrder(request):
    pk = request.GET.get("id")
    order = Order.objects.filter(pk=pk)
    if order.exists():
        order.delete()
        return HttpResponse("1")
    else:
        return HttpResponse("0")


def search(request):
    isShow = ['是', '否']
    if request.method == 'POST':
        data = json.loads(request.POST.get("data"))
        param = {v: obj['value'] for obj in data for k, v in obj.items() if k == "name"}
        page_length = int(param['length'])
        pattern = "[<|/|>|=|;|:|]"
        keyword = re.sub(pattern, '?',
                         param['search']['value'].replace(' ', '').replace('<p>', '?').replace('</p>', '?'))

        column = param['order'][0]['column']
        sorts = param['order'][0]['dir']
        if column == 6:
            if (sorts == "desc") | (sorts == "DESC"):
                order_by = "-createTime"
            else:
                order_by = "createTime"
        else:
            if (sorts == "desc") | (sorts == "DESC"):
                order_by = "-number"
            else:
                order_by = "number"

        res = Order.objects
        if "select-ordertype" in param:
            select_ordertype = param["select-ordertype"]
            if select_ordertype != '':
                res = res.filter(Q(typeId=select_ordertype))

        # 分词
        arr = " ".join(jieba.cut(keyword)).split(" ")
        q = Q(orderId__icontains=keyword) | Q(typeId__icontains=keyword)

        for kw in arr:
            q = q | Q(orderName__icontains=kw)

        if keyword in isShow:
            q = Q(isShow__icontains=keyword)

        total_length = res.filter(q).count()

        page_start = int(param['start'])
        page_end = page_start + page_length
        if page_length == -1:
            page_data = res.filter(q).order_by(order_by)
        else:
            page_data = res.filter(q).order_by(order_by)[
                        page_start: page_end]
        rest = {
            "iTotalRecords": page_length,  # 本次加载记录数量
            "iTotalDisplayRecords": total_length,  # 总记录数量
            "aaData": []}
    data = []
    for item in page_data:
        res = {'id': item.pk, 'typeId': item.typeId, 'orderId': item.orderId, 'orderName': item.orderName,
               'orderDescription': item.orderDescription, 'isShowOrder': item.isShowOrder, 'isShow': item.isShow,
               'typeDescription': item.typeDescription, 'number': item.number, 'createTime': item.createTime}
        data.append(res)
    rest['aaData'] = data

    return HttpResponse(json.dumps(rest, cls=DateEncoder, ensure_ascii=True), content_type='application/json')


@login_required(login_url="/xadmin/")
def edit(request):
    return render(request, "add.html")


def saveOrder(request):
    if "POST" == request.method:
        typeId = request.POST['typeId']
        operate = request.POST['operate']
        pk = request.POST['pk']
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

        updateOrderings = Order.objects.filter(typeId=typeId).filter(number__gte=number).order_by("number")

        num = int(number)
        for order in updateOrderings:
            num = num + 1
            order.number = num
            order.save()

        if "edit" == operate:
            order = Order.objects.get(pk=pk)
            order.delete()

        Order.objects.create(typeId=typeId, isShowOrder=isShowOrder, orderId=orderId, isShow=isShow,
                             orderName=orderName,
                             orderDescription=orderDescription,
                             typeDescription=typeDescription, number=number, createTime=timezone.now())

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
        OrderType.objects.create(typeId=typeId, typeName=typeName, number=number, createTime=timezone.now())
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
