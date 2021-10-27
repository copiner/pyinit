
"""
pip install xlrd
pip uninstall xlrd

author wdaonngg
read excel
"""

import xlrd

def read_excel():
    excel_tables = []
    file_name = './stuscore.xlsx'
    workbook = xlrd.open_workbook(file_name) # open file
    sheet = workbook.sheet_by_index(0) # sheet0
    print(file_name, sheet.name, sheet.nrows, sheet.ncols) # filename sheet's name ...
    print("line 2:", sheet.row_values(1))
    print("line 3:", sheet.col_values(2))

if __name__ == '__main__':
    # 读取Excel
    read_excel()
