'''
author wdaonngg
openpy
'''

import openpyxl

def read_excel(path, sheet_name):
    workbook = openpyxl.load_workbook(path)

    #sheet = workbook.sheetnames[sheet_name]
    sheet = workbook[sheet_name]

    a1=0
    b1=0
    c1=0
    d1=0
    e1=0
    f1=0

    a2=0
    b2=0
    c2=0
    d2=0
    e2=0
    f2=0

    a3=0
    b3=0
    c3=0
    d3=0
    e3=0
    f3=0

    a4=0
    b4=0
    c4=0
    d4=0
    e4=0
    f4=0

    a5=0
    b5=0
    c5=0
    d5=0
    e5=0
    f5=0

    a6=0
    b6=0
    c6=0
    d6=0
    e6=0
    f6=0

    a7=0
    b7=0
    c7=0
    d7=0
    e7=0
    f7=0

    a8=0
    b8=0
    c8=0
    d8=0
    e8=0
    f8=0

    a9=0
    b9=0
    c9=0
    d9=0
    e9=0
    f9=0

    a10=0
    b10=0
    c10=0
    d10=0
    e10=0
    f10=0

    a11=0
    b11=0
    c11=0
    d11=0
    e11=0
    f11=0

    a12=0
    b12=0
    c12=0
    d12=0
    e12=0
    f12=0


    for row in sheet.rows:
        #print('\n')
        #print(row[5].value)
        level = row[5].value
        if row[3].value == 1:

            if level == 'A':
                a1+=1
            elif level == 'B':
                b1+=1
            elif level == 'C':
                c1+=1
            elif level == 'D':
                d1+=1
            elif level == 'E':
                e1+=1
            else:
                f1+=1

        elif row[3].value == 2:

            if level == 'A':
                a2+=1
            elif level == 'B':
                b2+=1
            elif level == 'C':
                c2+=1
            elif level == 'D':
                d2+=1
            elif level == 'E':
                e2+=1
            else:
                f2+=1

        elif row[3].value == 3:

            if level == 'A':
                a3+=1
            elif level == 'B':
                b3+=1
            elif level == 'C':
                c3+=1
            elif level == 'D':
                d3+=1
            elif level == 'E':
                e3+=1
            else:
                f3+=1

        elif row[3].value == 4:

            if level == 'A':
                a4+=1
            elif level == 'B':
                b4+=1
            elif level == 'C':
                c4+=1
            elif level == 'D':
                d4+=1
            elif level == 'E':
                e4+=1
            else:
                f4+=1

        elif row[3].value == 5:

            if level == 'A':
                a5+=1
            elif level == 'B':
                b5+=1
            elif level == 'C':
                c5+=1
            elif level == 'D':
                d5+=1
            elif level == 'E':
                e5+=1
            else:
                f5+=1

        elif row[3].value == 6:

            if level == 'A':
                a6+=1
            elif level == 'B':
                b6+=1
            elif level == 'C':
                c6+=1
            elif level == 'D':
                d6+=1
            elif level == 'E':
                e6+=1
            else:
                f6+=1

        elif row[3].value == 7:

            if level == 'A':
                a7+=1
            elif level == 'B':
                b7+=1
            elif level == 'C':
                c7+=1
            elif level == 'D':
                d7+=1
            elif level == 'E':
                e7+=1
            else:
                f7+=1

        elif row[3].value == 8:

            if level == 'A':
                a8+=1
            elif level == 'B':
                b8+=1
            elif level == 'C':
                c8+=1
            elif level == 'D':
                d8+=1
            elif level == 'E':
                e8+=1
            else:
                f8+=1

        elif row[3].value == 9:

            if level == 'A':
                a9+=1
            elif level == 'B':
                b9+=1
            elif level == 'C':
                c9+=1
            elif level == 'D':
                d9+=1
            elif level == 'E':
                e9+=1
            else:
                f9+=1

        elif row[3].value == 10:

            if level == 'A':
                a10+=1
            elif level == 'B':
                b10+=1
            elif level == 'C':
                c10+=1
            elif level == 'D':
                d10+=1
            elif level == 'E':
                e10+=1
            else:
                f10+=1

        elif row[3].value == 11:

            if level == 'A':
                a11+=1
            elif level == 'B':
                b11+=1
            elif level == 'C':
                c11+=1
            elif level == 'D':
                d11+=1
            elif level == 'E':
                e11+=1
            else:
                f11+=1

        elif row[3].value == 12:

            if level == 'A':
                a12+=1
            elif level == 'B':
                b12+=1
            elif level == 'C':
                c12+=1
            elif level == 'D':
                d12+=1
            elif level == 'E':
                e12+=1
            else:
                f12+=1

        else:

            print(row[3].value)
            print()


    print('Class 1 \n')
    print('A1 = ', a1)
    print('B1 = ', b1)
    print('C1 = ', c1)
    print('D1 = ', d1)
    print('E1 = ', e1)
    print('F1 = ', f1)
    print('A1 + B1 = ',a1+b1)
    print('D1 + E1 = ',d1+e1)
    print('\n')

    print('Class 2 \n')
    print('A2 = ', a2)
    print('B2 = ', b2)
    print('C2 = ', c2)
    print('D2 = ', d2)
    print('E2 = ', e2)
    print('F2 = ', f2)
    print('A2 + B2 = ',a2+b2)
    print('D2 + E2 = ',d2+e2)
    print('\n')

    print('Class 3 \n')
    print('A3 = ', a3)
    print('B3 = ', b3)
    print('C3 = ', c3)
    print('D3 = ', d3)
    print('E3 = ', e3)
    print('F3 = ', f3)
    print('A3 + B3 = ',a3+b3)
    print('D3 + E3 = ',d3+e3)
    print('\n')

    print('Class 4 \n')
    print('A4 = ', a4)
    print('B4 = ', b4)
    print('C4 = ', c4)
    print('D4 = ', d4)
    print('E4 = ', e4)
    print('F4 = ', f4)
    print('A4 + B4 = ',a4+b4)
    print('D4 + E4 = ',d4+e4)
    print('\n')

    print('Class 5 \n')
    print('A5 = ', a5)
    print('B5 = ', b5)
    print('C5 = ', c5)
    print('D5 = ', d5)
    print('E5 = ', e5)
    print('F5 = ', f5)
    print('A5 + B5 = ',a5+b5)
    print('D5 + E5 = ',d5+e5)
    print('\n')

    print('Class 6 \n')
    print('A6 = ', a6)
    print('B6 = ', b6)
    print('C6 = ', c6)
    print('D6 = ', d6)
    print('E6 = ', e6)
    print('F6 = ', f6)
    print('A6 + B6 = ',a6+b6)
    print('D6 + E6 = ',d6+e6)
    print('\n')

    print('Class 7 \n')
    print('A7 = ', a7)
    print('B7 = ', b7)
    print('C7 = ', c7)
    print('D7 = ', d7)
    print('E7 = ', e7)
    print('F7 = ', f7)
    print('A7 + B7 = ',a7+b7)
    print('D7 + E7 = ',d7+e7)
    print('\n')

    print('Class 8 \n')
    print('A8 = ', a8)
    print('B8 = ', b8)
    print('C8 = ', c8)
    print('D8 = ', d8)
    print('E8 = ', e8)
    print('F8 = ', f8)
    print('A8 + B8 = ',a8+b8)
    print('D8 + E8 = ',d8+e8)
    print('\n')

    print('Class 9 \n')
    print('A9 = ', a9)
    print('B9 = ', b9)
    print('C9 = ', c9)
    print('D9 = ', d9)
    print('E9 = ', e9)
    print('F9 = ', f9)
    print('A9 + B9 = ',a9+b9)
    print('D9 + E9 = ',d9+e9)
    print('\n')

    print('Class 10 \n')
    print('A10 = ', a10)
    print('B10 = ', b10)
    print('C10 = ', c10)
    print('D10 = ', d10)
    print('E10 = ', e10)
    print('F10 = ', f10)
    print('A10 + B10 = ',a10+b10)
    print('D10 + E10 = ',d10+e10)
    print('\n')

    print('Class 11 \n')
    print('A11 = ', a11)
    print('B11 = ', b11)
    print('C11 = ', c11)
    print('D11 = ', d11)
    print('E11 = ', e11)
    print('F11 = ', f11)
    print('A11 + B11 = ',a11+b11)
    print('D11 + E11 = ',d11+e11)
    print('\n')

    print('Class 12 \n')
    print('A12 = ', a12)
    print('B12 = ', b12)
    print('C12 = ', c12)
    print('D12 = ', d12)
    print('E12 = ', e12)
    print('F12 = ', f12)
    print('A12 + B12 = ',a12+b12)
    print('D12 + E12 = ',d12+e12)
    print('\n')

    sheet.append(["A","B","C","D","E","F","A+B","D+E"])

    for i in range(12):
        sheet.append([9,v,1,9])

    workbook.save(filename=path)

book_name = "stuscore.xlsx";
sheet_name = '成绩';

read_excel(book_name, sheet_name)
