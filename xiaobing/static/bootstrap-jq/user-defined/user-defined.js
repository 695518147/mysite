var xiaobing = (function () {

    //缓冲对象容器
    var orders = {};

    /***
     * 显示右侧内容
     * @param dom
     */
    function showContent(dom) {
        var id = dom.id;
        var order;
        if ((id in orders) || (orders[id] && orders[id] != '')) {
            order = orders[id];
            if (order["isShow"] == 'false') {
                $("#content2").empty().html(order.typeDescription);
                $("#content1").hide();
                $("hr").hide();
            } else {
                $("#content1").show();
                $("hr").show();
                $("#content1").empty().html(order.typeDescription);
                $("#content2").empty().html(order.orderDescription);
            }
        } else {
            $.ajax({
                type: "GET",
                url: "/xiaobing/getOrderById/",

                // 允许携带证书
                xhrFields: {
                    withCredentials: true
                },
                // 允许跨域
                crossDomain: true,
                data: {'orderId': id}
            }).done(function (data) {
                var json = JSON.parse(data);
                order = json[0].fields;
                orders[id] = order;
                if (order["isShow"] == 'false') {
                    $("#content2").empty().html(order.typeDescription);
                    $("#content1").hide();
                    $("hr").hide();
                } else {
                    $("#content1").show();
                    $("hr").show();
                    $("#content1").empty().html(order.typeDescription);
                    $("#content2").empty().html(order.orderDescription);
                }
            }).fail(function (err) {

            });
        }
        $(dom).addClass("meun-item-active").siblings().removeClass("meun-item-active");
    }

    /**
     * 初始化头部tab
     */
    function initTopTab() {
        $.ajax({
            type: "GET",
            url: "/xiaobing/getAllOrderType/",

            // 允许携带证书
            xhrFields: {
                withCredentials: true
            },
            // 允许跨域
            crossDomain: true
        }).done(function (data) {
            var json = JSON.parse(data);
            var arr = [];
            $.each(json, function (index, orderType) {
                var li = '<li role="presentation" class="' + (index == 0 ? "active" : "") + '" id="' + orderType.fields.typeId + '"><a href="#">' + orderType.fields.typeName + '</a></li>';
                arr.push(li)
            });
            $("#tab_header").empty()
                .append(arr.join(" "))
                .find("li")
                .on("click", function () {
                    $(this).addClass("active").siblings().removeClass("active");
                    initLeftMeun(this.id);
                });
            $("#tab_header").find("li.active").trigger('click');
        });
    }

    /**
     * 初始化左侧菜单
     * @param typeId
     */
    function initLeftMeun(typeId) {
        document.cookie = "csrfmiddlewaretoken=" + $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "GET",
            url: "/xiaobing/getAllOrderByTypeId/",

            // 允许携带证书
            xhrFields: {
                withCredentials: true
            },
            // 允许跨域
            crossDomain: true,
            data: {'typeId': typeId}
        }).done(function (data) {
            var json = JSON.parse(data);
            $("#leftMeun").empty();
            $.each(json, function (index, data) {
                var order = data.fields;
                var item = '<div class="meun-item ' + (index == 0 ? " meun-item-active" : "") + '" ' +
                    'id="' + order.orderId + '" onclick="xiaobing.showContent(this)" href="#" name=' + order.typeId + ' role="tab" data-toggle="tab">' +
                    '<div id="lineHight">' + order.orderName + '</div> </div>';
                if (index == 0) {
                    if (order["isShow"] == 'false') {
                        $("#content2").empty().html(order.typeDescription);
                        $("#content1").hide();
                        $("hr").hide();
                    } else {
                        $("#content1").show();
                        $("hr").show();
                        $("#content1").empty().html(order.typeDescription);
                        $("#content2").empty().html(order.orderDescription);
                    }
                }
                $("#leftMeun").append(item)
            });

        });
    }

    return {
        showContent: function (dom) {
            showContent(dom)
        },
        initTopTab: function () {
            initTopTab()
        }
    }
})();