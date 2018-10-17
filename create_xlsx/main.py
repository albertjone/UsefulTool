##!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlsxwriter

class Header(object):
    def __init__(self,
                 name,
                 start_num,
                 length,
                 end_num,
                 *child_headers):
        self.name = name
        self.start_num = start_num
        self.length = length
        self.end_num = end_num
        self.child_headers = child_headers

def write_table_heads(worksheet, headers):
    maps = {0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            }
    merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})
    for header in headers:
        if len(header.child_headers) <= 0:
            worksheet.merge_range(0, 
                                  header.start_num,
                                  1,
                                  header.end_num,
                                  header.name,
                                  merge_format)
        else:
            worksheet.merge_range(0,
                                  header.start_num,
                                  0,
                                  header.end_num,
                                  header.name,
                                  merge_format)
            num =  header.start_num - 1
            for child in header.child_headers:
                num += 1
                worksheet.write_string(1, num, child)

def write_item(worksheet, item, headers):
    size = [len(item[key]) for key in item.keys() if (len(item[key]) > 1)]
    for header in headers:
        name = header.name
        if len(header.child_headers) <= 0:
            worksheet.merge_cell(1,
                                header.start_num,
                                1 + size,
                                header.end_num,
                                item[name])
        else:
            childs = header.child_headers
            start = header.start_num
            for x in range(2, 2 + size):
                for y in range(start, 
                               start - 1 + len(header.child_headers)):
                    worksheet.write_string(x, y, item[name][x][childs[y - start]])

def create_xlsx(file_name=None,path=None,data=None):
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet(file_name)
    headers = []
    necessary_headers = [
        'email',
        'phone',
        'resources'
    ]
    optional_headers = []
    start_num = 0
    headers_check = data[0].keys()
    for key in headers_check:
        child_headers = []
        length = 0
        for value in headers_check:
            length += 1
            child_headers.append(value) 
        if len(child_headers) == 0:
            length = 1
        if start_num > 0:
            start_num += length
        headers.append(Header(name=key,
                              start_num=start_num,
                              length=length,
                              end_num=length - 1 + start_num,
                              child_headers=child_headers))
        if key not in necessary_headers:
            optional_headers.append(key)
    write_table_heads(worksheet, headers)

    for item in data:
        write_item(worksheet, item, headers)

def main():
    file_name = "hi.xlsx"
    data = []
    create_xlsx(file_name, data)

if __name__=="__name__":
    main()