import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('test')
worksheet.merge_range(0, 0, 1, 1, "mergeCells")

workbook.close()