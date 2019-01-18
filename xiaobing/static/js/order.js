$(function () {

    //配置DataTables默认参数
    $.extend(true, $.fn.dataTable.defaults, {
        language: {
            url: "/Chinese.json"
        },
        "dom": "<'row'<'col-sm-8'l><'col-sm-4'<'#toolbar'>f>><'row'<'col-sm-12'tr>><'row'<'col-sm-5'i><'col-sm-7'p>>"
    });
    order.init();
});

var order = (function () {
    var mytable;

    /**
     * 初始化表格
     */
    function initTable() {
        mytable = $("#datatable").DataTable({
            sSource: "/xiaobing/search/",
            serverSide: true,
            bInfo: true,
            //服务器端，数据回调处理
            fnServerData: function (sSource, aDataSet, fnCallback) {
                $.ajax({
                    "dataType": 'json',
                    "type": "post",
                    "url": "/xiaobing/search/",
                    "data": {data: JSON.stringify(aDataSet)},
                    "success": function (resp) {
                        fnCallback(resp);
                    }
                });
            },
            "aLengthMenu": [[5, 10, 25, 50, 100, -1], [5, 10, 25, 50, 100, "All"]], // 定义每页显示数据数量
            aoColumns: [
                {mData: "orderName", "width": 40, "title": "指令名称"},
                {mData: "orderId", "width": 40, "title": "指令代码"},
                {
                    mData: "typeId",
                    "width": 40,
                    "visible": true,
                    "title": "指令类别",
                    "defaultContent": "<i>Not set</i>"
                },
                {mData: "orderDescription", "width": 40, "title": "指令说明"},
                {mData: "typeDescription", "width": 40, "title": "类别说明"},
                {mData: "isShowOrder", "width": 40, "title": "是否显示"},
                {mData: "createTime", "width": 40, "title": "创建时间"},
                {mData: "", "width": 40, "title": "操作"},
            ],
            columnDefs: [
                {
                    targets: [5],
                    render: function (data, type, row, meta) {
                        return data == "true" ? "是" : "否";
                    },
                },
                {
                    targets: [0, 1, 2, 3, 4, 5, 7],
                    orderable: false,
                    ordering: false
                },
                {
                    targets: [7],
                    render: function (data, type, row, meta) {
                        var str = escape(JSON.stringify(row))
                        var arr = [];
                        arr.push('<button type="button" style="margin-left:10px" order=' + str + ' class="btn btn-primary" onclick="order.updateRow(this)">修改</button>')
                        arr.push('<button type="button" style="margin-left:10px" order=' + str + ' class="btn btn-danger" onclick="order.deleteRow(this)">删除</button>')
                        return arr.join(" ");
                    },
                }
            ],
            // 是否允许检索
            searching: true,
            // 是否允许排序
            ordering: true,
            //默认最后一列（最后更新时间）降序排列
            order: [[5, "ASC"]],
            // 是否允许翻页，设成false，翻页按钮不显示
            scrollX: false,
            scrollY: false,
            autoWidth: true,
            processing: false,

            initComplete: function (settings, json) {
                $("input[type=search]").addClass("form-control1");
                $("#toolbar").append("<a href='JavaScript:void(0)' " +
                    "class='btn btn-primary btn-sm'  onclick=\"order.modalHandler('orderModal','add')\">新建指令</a>");
            },
            rowCallback: function (row, data, displayNum, displayIndex, dataIndex) {
                $(row).find("video,img").addClass("adapt");
            }
        });

    }

    /**
     * 模态框数据回显
     * @param domId
     * @param callback   用于修改时数据回显
     * @param operate
     */
    function modalHandler(domId, callback, operate) {
        $("#" + domId).modal({backdrop: 'static', keyboard: false});

        //edit
        if (arguments.length > 1 && typeof callback === "function") {
            callback()
        }

        //add
        if (arguments.length > 1 && typeof callback === "string") {
            operate = callback
            $("#operate").val(operate)
            $("#id").val("");
            UE.getEditor("orderDescription").setContent( "" )
            UE.getEditor("orderName").setContent( "" )
            UE.getEditor("typeDescription").setContent( "" )
        }

        //edit
        if (arguments.length > 2 && typeof operate === "string") {
            $("#operate").val(operate)
        }
    }


    function init() {
        instanceUE('orderName');
        instanceUE('orderDescription');
        instanceUE('typeDescription');
        instanceUE('typeName');

        $.get("/xiaobing/getAllOrderType/").done(function (data) {
            var json = JSON.parse(data);
            var arr = [];
            $.each(json, function (index, order) {
                var option = '<option value="' + order.fields.typeId + '">' + order.fields.typeName + '</option>';
                arr.push(option)
            });
            $("#typeId").empty().append(arr.join())

        });

        initTable();

    }

    function instanceUE(id) {
        var ue = UE.getEditor(id, {
            'toolbars': [['source', '|', 'undo', 'redo', '|', 'bold', 'italic', 'underline', 'formatmatch', 'autotypeset', '|', 'forecolor', 'backcolor', '|', 'link', 'unlink', '|', 'simpleupload', 'insertvideo', 'music', 'attachment', 'map']],
            'a': 2,
            'serverUrl': '/ueditor/controller/?imagePathFormat=image%2Forder&filePathFormat=bb%2F'
        });
    }

    function deleteRow(dom) {

        var index = layer.confirm('确认删除吗？', {
            btn: ['确认', '取消'] //按钮
        }, function () {
            var order = JSON.parse(unescape($(dom).attr("order")));
            $.ajax({
                type: "GET",
                url: "/xiaobing/deleteOrder/",
                // 允许携带证书
                xhrFields: {
                    withCredentials: true
                },
                // 允许跨域
                crossDomain: true,
                data: {id: order.id}
            }).done(function () {
                mytable.draw()

            }).done(function () {
                layer.close(index);
                layer.msg('删除成功！', {
                    time: 2000 //20s后自动关闭
                });
            }).fail(function (err) {

            });
        }, function () {

        });
    }

    function updateRow(dom) {
        var order = JSON.parse(unescape($(dom).attr("order")));
        modalHandler("orderModal", function () {
            $("#typeId").val(order.typeId);
            $("#orderId").val(order.orderId);
            if (order.isShowOrder == "true") {
                $("#isShowOrder").attr("checked", "checked");
            } else {
                $("#isShowOrder").removeAttr("checked");
            }
            if (order.isShow == "true") {
                $("#isShow").attr("checked", "checked");
            } else {
                $("#isShow").removeAttr("checked");
            }
            $("#number").val(order.number);
            $("#id").val(order.id);
            UE.getEditor('orderName').setContent(order.orderName);
            UE.getEditor('orderDescription').setContent(order.orderDescription);
            UE.getEditor('typeDescription').setContent(order.typeDescription);

        }, 'edit');
    }


    function saveOrder() {
        document.cookie = "csrfmiddlewaretoken=" + $("input[name=csrfmiddlewaretoken]").val();
        var typeId = document.getElementById("typeId").value;
        var isShow = $("#isShow").prop("checked");
        var isShowOrder = $("#isShowOrder").prop("checked");
        var operate = $("#operate").val();
        var pk = $("#id").val();
        var orderName = getContent('orderName');
        var orderNameText = getContentText('orderName');
        var number = document.getElementById("number").value;
        var orderDescription = getContent('orderDescription');
        var typeDescription = getContent('typeDescription');

        var order = {
            pk: pk,
            typeId: typeId,
            isShow: isShow,
            operate: operate,
            isShowOrder: isShowOrder,
            orderName: orderName,
            orderNameText: orderNameText,
            number: number,
            orderDescription: orderDescription,
            typeDescription: typeDescription
        };


        $.ajax({
            type: "POST",
            url: "/xiaobing/saveOrder/",
            // 允许携带证书
            xhrFields: {
                withCredentials: true
            },
            // 允许跨域
            crossDomain: true,
            data: order
        }).done(function (data) {
            mytable.draw();
            $("#orderModal").modal('hide');
        }).done(function () {
            if (operate == 'add') {
                layer.msg('添加成功！', {
                    time: 2000 //20s后自动关闭
                });
            } else {
                layer.msg('修改成功！', {
                    time: 2000 //20s后自动关闭
                });
            }

        });
    }

    function saveOrderType() {
        document.cookie = "csrfmiddlewaretoken=" + $("input[name=csrfmiddlewaretoken]").val();
        var typeName = getContent("typeName");
        var typeNameText = getContentText("typeName");
        var number = document.getElementById("typeNumber").value;

        var orderType = {
            typeName: typeName,
            typeNameText: typeNameText,
            number: number
        };

        $.ajax({
            type: "POST",
            url: "/xiaobing/saveType/",
            // 允许携带证书
            xhrFields: {
                withCredentials: true
            },
            // 允许跨域
            crossDomain: true,
            data: orderType
        }).done(function (data) {
            var json = JSON.parse(data);
            var arr = [];
            $.each(json, function (index, order) {
                var option = '<option value="' + order.fields.typeId + '">' + order.fields.typeName + '</option>';
                arr.push(option)
            });
            $("#typeId").empty().append(arr.join());
            $("#myModal").modal('hide');

        }, 'json').done(function () {
            layer.msg('添加成功！', {
                time: 2000 //20s后自动关闭
            });
        });
    }

    function getContent(id) {
        return UE.getEditor(id).getContent();
    }

    function getContentText(id) {
        return UE.getEditor(id).getContentTxt();
    }

    return {
        init: function () {
            init()
        },
        initTable: function () {
            initTable()
        },
        deleteRow: function (dom) {
            deleteRow(dom)
        },
        updateRow: function (dom) {
            updateRow(dom)
        },
        modalHandler: function (domId, callback, operate) {
            modalHandler(domId, callback, operate)
        },
        saveOrder: function () {
            saveOrder()
        },
        saveOrderType: function () {
            saveOrderType()
        }
    }
})();




