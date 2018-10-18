#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding=utf-8 -*-

import main


class Order(object):
    def __init__(self, email="", phone=""):
        self.email = email
        self.phone = phone
        self.resources = []

    def set_resources(self, *args):
        for arg in args:
            self.resources.append(arg)


data = [
    {
        "email": "guan.xiaojue@99cloud.net",
        "phone": "",
        "resources": [
            {
                "type": "instance",
                "name": "test-instance1",
                "project": "default"
            }, {
                "type": "instance",
                "name": "test-instance1",
                "project": "default"
            }
        ],
        "overdue_days": 12
    }, {
        "email": "guan.xiaojue@99cloud.net",
        "phone": "",
        "resources": [
            {
                "type": "instance",
                "name": "test-instance1",
                "project": "default"
            }
        ],
        "overdue_days": 12
    }
]

data = [
    {
        "email": "guan.xiaojue@99cloud.net",
        "phone": "1881",
        "resources": [
            {
                u"默认": u"默认",
                "name": "test-instance1",
                "project": ""
            }, {
                "type": "instance",
                "name": "test-instance1",
                "project": "default"
            }
        ],
        "overdue_days": 12
    },
    {
        "email": "guan.xiaojue@99cloud.net",
        "phone": "",
        "resources": [
            {
                "type": "",
                "name": "test-instance1",
                "project": "default"
            }, {
                "type": "instance",
                "name": "test-instance1",
                "project": "default"
            }
        ],
        "overdue_days": 12
    }
]

# data = [
#     {
#         "email": "guan.xiaojue@99cloud.net",
#         "phone": "1881",
#         "resources": [],
#         "overdue_days": 12
#     }
# ]

# data = [
#     {
#         "email": "guan.xiaojue@99cloud.net",
#         "phone": "1881",
#         "overdue_days": 12
#     }
# ]

# data = [
#     {
#         "overdue_days": 12,
#         "resources": [
#             {
#                 "type": "instance",
#                 "name": "test-instance1",
#                 "project": "default"
#             }, {
#                 "type": "instance",
#                 "name": "test-instance1",
#                 "project": "default"
#             }
#         ],
#     }
# ]
resources = [
    {'num': 1,
     '资源类型': '云主机',
     'resource_name': 'instance1',
     'project_name': 'project1'
     },
    {'num': 2,
     'resource_type': '云主机',
     'resource_name': 'instance1',
     'project_name': 'project1'
     },
    {'num': 3,
     'resource_type': '云主机',
     'resource_name': 'instance1',
     'project_name': 'project1'
     },
    {'num': 4,
     'resource_type': '云主机',
     'resource_name': 'instance1',
     'project_name': 'project1'
     }
]
# order = Order('1426473620@qq.com', '18816208298')
# order.set_resources(resources)
# print data[0].keys()
# main.create_xlsx('test1.xlsx', data)
import create_xlsx
# create_xlsx.create_xlsx('test3.xlsx', data)
# data = create_xlsx.json_to_obj(data)
# print datax
# print dir(data)
import json
print(json.dumps(resources, encoding='UTF-8',
                 ensure_ascii=False, sort_keys=False, indent=4))

students = {
    '小甲':18,
    '小乙':20,
    '小丙':15
}
print 
b = [ key for key,value in students.items() ]
print b