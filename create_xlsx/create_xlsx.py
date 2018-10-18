#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-*- coding=utf-8 -*-
import xlsxwriter
import json


def create_xlsx(file_name, data):
    # data = json.dumps(data,encoding='UTF-8', ensure_ascii=False)
    write_header = True
    firt_row = True
    row_point = 0
    wbook = xlsxwriter.Workbook(file_name)
    wsheet = wbook.add_worksheet(file_name)
    for item in data:
        item_size = 1
        for key in item.keys():
            if type(item[key]) is list:
                item_size = len(item[key]) if len(item[key]) else item_size
        col_point = 0
        for key in item.keys():
            if type(item[key]) is list:
                if firt_row and write_header:
                    row_point = 0
                    wsheet.merge_range(row_point,
                                       col_point,
                                       0,
                                       (col_point + len(item[key][0].keys())
                                        ) if len(item[key]) != 0 else 1,
                                       key)
                    row_point = 2
                if len(item[key]) > 0:
                    for c_key in item[key][0]:
                        if firt_row and write_header:
                            row_point = 1
                            wsheet.write(row_point,
                                         col_point,
                                         c_key)
                            row_point = 2
                        for row_add in range(0, item_size):
                            wsheet.write(row_point + row_add,
                                         col_point,
                                         item[key][row_add][c_key])
                        col_point += 1
                continue
            if firt_row and write_header:
                row_point = 0
                wsheet.merge_range(row_point,
                                   col_point,
                                   row_point + 1,
                                   col_point,
                                   key)
                row_point = 2
            if item_size == 1:
                wsheet.write(row_point,
                             col_point,
                             item[key])
            wsheet.merge_range(row_point,
                               col_point,
                               row_point + item_size - 1,
                               col_point,
                               item[key])
            col_point += 1
        if firt_row and write_header:
            firt_row = False
        row_point += item_size
    wbook.close()


# def create_xlsx(file_name, data):
#     wbook = xlsxwriter.Workbook(file_name)
#     wsheet = wbook.add_worksheet(file_name)
#     start_row = 2
#     item_num = 0
#     for item in data:
#         headers = []
#         item_size = 0
#         for key in item.keys():
#             key = key.decode('utf-8')
#             length = 1
#             if type(item[key]) is list:
#                 if len(item[key]) > 0:
#                     length = len(item[key][0])
#                     item_size = len(item[key])
#                     headers.append({
#                         key: [length, [ckey.decode('utf-8') for ckey in item[key][0].keys()]]
#                     })
#                     continue
#             headers.append({key: length})
#         if item_num <= 0:
#             head_start_col = 0
#             for header in headers:
#                 if type(header.values()[0]) is list:
#                     length = header.values()[0][0]
#                 else:
#                     length = header.values()[0]
#                 head_end_col = head_start_col + length - 1
#                 if length == 1:
#                     wsheet.merge_range(0,
#                                        head_start_col,
#                                        1,
#                                        head_end_col,
#                                        header.keys()[0])
#                 else:
#                     wsheet.merge_range(0,
#                                        head_start_col,
#                                        0,
#                                        head_end_col,
#                                        header.keys()[0])
#                     for child_num in range(0, length):
#                         wsheet.write(1,
#                                      head_start_col + child_num,
#                                      header.values()[0][1][child_num])
#                 head_start_col += length

#         start_col = 0
#         for header in headers:
#             if type(header.values()[0]) is list:
#                 length = header.values()[0][0]
#             else:
#                 length = header.values()[0]
#             if length == 1:
#                 end_row = item_size + start_row - 1
#                 end_col = start_col + header.values()[0] - 1
#                 if end_col - start_col == 0 and end_row - start_row == 0:
#                     wsheet.write(start_row,
#                                  start_col,
#                                  item[header.keys()[0]])
#                 else:
#                     wsheet.merge_range(start_row,
#                                        start_col,
#                                        end_row,
#                                        end_col,
#                                        item[header.keys()[0]])
#             else:
#                 for x in range(0, item_size):
#                     for y in range(0, length):
#                         wsheet.write(x+start_row,
#                                      y+start_col,
#                                      item[header.keys()[0]][x][header.values()[0][1][y]])
#             start_col += length
#         start_row += item_size
#         item_num += 1
#     wbook.close()
