arr = [
    {"name": "draw", "value": 1},
    {"name": "columns", "value": [
        {"data": "orderName", "name": "", "searchable": True, "orderable": False,
         "search": {"value": "", "regex": False}
         },
        {"data": "typeId", "name": "", "searchable": False, "orderable": True, "search": {"value": "", "regex": False}},
        {"data": "orderId", "name": "", "searchable": True, "orderable": False,
         "search": {"value": "", "regex": False}},
        {"data": "orderDescription", "name": "", "searchable": True, "orderable": False,
         "search": {"value": "", "regex": False}},
        {"data": "typeDescription", "name": "", "searchable": True, "orderable": False,
         "search": {"value": "", "regex": False}},
        {"data": "isShowOrder", "name": "", "searchable": True, "orderable": False,
         "search": {"value": "", "regex": False}},
        {"data": "createTime", "name": "", "searchable": True, "orderable": True,
         "search": {"value": "", "regex": False}
         },
        {"data": "", "name": "", "searchable": True, "orderable": False, "search": {"value": "", "regex": False}}
    ]
     },
    {"name": "order", "value": [{"column": 5, "dir": "ASC"}]
     },
    {"name": "start", "value": 0},
    {"name": "length", "value": 5},
    {"name": "search", "value": {"value": "", "regex": False}}
]

o = {v: obj['value'] for obj in arr for k, v in obj.items() if k == "name"}

print(o)
