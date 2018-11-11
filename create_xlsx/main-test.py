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

# data = [
#     {
#         "email": "guan.xiaojue@99cloud.net",
#         "phone": "1881",
#         "resources": [
#             {
#                 "type": u"默认",
#                 "name": "test-instance1",
#                 "project": ""
#             }, {
#                 "type": "instance",
#                 "name": "test-instance1",
#                 "project": "default"
#             }
#         ],
#         "overdue_days": 12
#     },
#     {
#         "email": "guan.xiaojue@99cloud.net",
#         "phone": "",
#         "resources": [
#             {
#                 "type": "",
#                 "name": "test-instance1",
#                 "project": "default"
#             }, {
#                 "type": "instance",
#                 "name": "test-instance1",
#                 "project": "default"
#             }
#         ],
#         "overdue_days": 12
#     }
# ]

data = [
    {
        u"邮件": u"还好",
        "phone": "1881",
        "resources": [],
        "overdue_days": 12
    }
]

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


import create_xlsx
create_xlsx.create_xlsx('test3.xlsx', data)
