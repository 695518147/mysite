## datatable 服务端返回数据格式
```
result = {
    "iTotalRecords": page_length,  # 本次加载记录数量
    "iTotalDisplayRecords": total_length,  # 总记录数量
    "aaData": []
    }
```

## dom的使用
```
1. `l` 代表 length，左上角的改变每页显示条数控件
2. `f` 代表 filtering，右上角的过滤搜索框控件
3. `t` 代表 table，表格本身
4. `i` 代表 info，左下角的表格信息显示控件
5. `p` 代表 pagination，右下角的分页控件
6. `r` 代表 processing，表格中间的数据加载等待提示框控件
7. `B` 代表 button，Datatables可以提供的按钮控件，默认显示在左上角

Datatables自己定义的，通过这三个标签，Datatables就可以任你摆布了
1. < > - 这个尖括号就代表 html标签里的  <div></div>
2. <"className" > - 代表添加了class的div  <div class="className"></div>
3. <"#id" > - 代表添加了id的div <div id="id"></div>
```