'''
openpy
'''

import openpyxl

def read_excel(path, sheet_name):
    workbook = openpyxl.load_workbook(path)
    
    #sheet = workbook.sheetnames[sheet_name]
    sheet = workbook[sheet_name]

    for row in sheet.iter_rows(min_row=3, max_col=6, max_row=4):
        for cell in row:
            print(cell)
   # print(sheet.tables)


book_name = "./stuscore.xlsx";
sheet_name = '成绩';

read_excel(book_name, sheet_name)
