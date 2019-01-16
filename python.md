## 1.序列化问题
- TypeError: Object of type datetime is not JSON serializable
> 使用python自带的json，将数据转换为json数据时，datetime格式的数据报错：datetimeTypeError: datetime.datetime(2017, 3, 21, 2, 11, 21) is not JSON serializable。  
> 2、解决方法
> 就是重写构造json类，遇到日期特殊处理，其余的用内置的就行。
> 用处： xiaobing.view.py   74行。


## 2.python的str，unicode对象的encode和decode方法
