'''
author wdaonngg
write
append
excel
'''

import openpyxl

tfi = 'summary.xlsx'
#wb = openpyxl.Workbook()
wb = openpyxl.load_workbook(tfi)


wsheet = wb['sum']

'''
for row in range(1, 10):
    wsheet.append(range(10));
'''

v=1
listc = [9,v,1,9]
for i in range(12):
    wsheet.append(listc)

#wsheet.append([2,2,3])
#wsheet.append((2,3,7,1,9,1,1))

wb.save(filename=tfi)
