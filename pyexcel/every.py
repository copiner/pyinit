'''
author wdaonngg
every
'''

import openpyxl

import math

def filter_excel(book_name, sheet_name):

    workbook = openpyxl.load_workbook(book_name)
    sheet = workbook[sheet_name]

    lclass = ['01','02','03','04','05','06','07','08','09','10','11','12']
    #lclass = ['01']
    head1 = []#first line
    head2 = []# second line

    for row in sheet.rows:
        trow = [] #清空

        if row[0].value == '信息':#第一行表头
            for cell in row:
                head1.append(cell.value)

        elif row[0].value == '学号': #第二行表头
            for cell in row:
                head2.append(cell.value)

            #创建sheet 添加表头
            for sname in lclass:
                workbook.create_sheet(sname)
                workbook[sname].append(head1)
                workbook[sname].append(head2)
        else:
            #sheet 添加内容
            for cell in row:
                trow.append(cell.value)

            c = row[3].value # int print(isinstance(c,int))

            if c:
                if c > 9:
                    workbook[str(c)].append(trow)
                else:
                    workbook['0'+str(c)].append(trow)


    workbook.save(filename=book_name)

def cal_excel(book_name):

    workbook = openpyxl.load_workbook(book_name)
    lclass = ['01','02','03','04','05','06','07','08','09','10','11','12']

    # 计算
    lhead = [
        "班级","学籍人数","参考人数","班主任",
        "平均分","平均分名次","班级前70%人数","班级前70%平均分","班级前70%平均分名次",
        "A人数","A率","A率名次","AB人数","AB率","AB率名次","DE人数","DE率","DE率名次",
        "班级前70%AB人数","班级前70%AB率","班级前70%AB率名次"]

    # workbook.create_sheet("汇总")
    # workbook["汇总"].append(lhead1)

    #sheet.max_row-2
    sheet = workbook['01']
    t_stu = sheet.max_row-2 #总人数 total stu
    t_stu70 = math.ceil((sheet.max_row-2)*0.7) #前70%总人数

    #总分
    t_sco = 0 #总分 score
    t_aver = 0 # 平均分 total average

    a_stu = 0 #A人数
    a_ratio = 0 #A率
    b_stu = 0 #B人数
    d_stu = 0 #D人数
    e_stu = 0 #E人数

    ab_stu = 0 #AB人数
    ab_ratio = 0 #AB率

    de_stu = 0 #DE人数
    de_ratio = 0 #DE率

    t_sco70 = 0 #人数前70%总分
    t_aver70 = 0 #总人数前70%平均分

    a_stu70 = 0 #前70% A人数
    b_stu70 = 0 #前70% B人数
    ab_stu70 = 0 #前70%  AB人数
    ab_ratio70 = 0 #前70%  AB率

    #语文chinese
    ct_sco = 0 #语文总分 score
    ct_aver = 0 # 平均分 total average
    ct_sco70 = 0 #人数前70%总分
    ct_aver70 = 0 #人数前70%平均分

    ca_stu = 0 #A人数
    ca_ratio = 0 #A率

    cab_stu = 0 #AB人数
    cab_ratio = 0 #AB率


    cde_stu = 0 #AB人数
    cde_ratio = 0 #AB率

    cab_stu70 = 0 #AB人数
    cab_ratio70 = 0 #AB率

    #数学math
    mt_sco = 0 #语文总分 score
    mt_aver = 0 # 平均分 total average
    mt_sco70 = 0 #人数前70%总分
    mt_aver70 = 0 #人数前70%平均分

    ma_stu = 0 #A人数
    ma_ratio = 0 #A率

    mab_stu = 0 #AB人数
    mab_ratio = 0 #AB率


    mde_stu = 0 #AB人数
    mde_ratio = 0 #AB率

    mab_stu70 = 0 #AB人数
    mab_ratio70 = 0 #AB率

    #英语 english
    et_sco = 0 #语文总分 score
    et_aver = 0 # 平均分 total average
    et_sco70 = 0 #人数前70%总分
    et_aver70 = 0 #人数前70%平均分

    ea_stu = 0 #A人数
    ea_ratio = 0 #A率

    eab_stu = 0 #AB人数
    eab_ratio = 0 #AB率


    ede_stu = 0 #AB人数
    ede_ratio = 0 #AB率

    eab_stu70 = 0 #AB人数
    eab_ratio70 = 0 #AB率

    #科学
    st_sco = 0 #语文总分 score
    st_aver = 0 # 平均分 total average
    st_sco70 = 0 #人数前70%总分
    st_aver70 = 0 #人数前70%平均分

    sa_stu = 0 #A人数
    sa_ratio = 0 #A率

    sab_stu = 0 #AB人数
    sab_ratio = 0 #AB率


    sde_stu = 0 #AB人数
    sde_ratio = 0 #AB率

    sab_stu70 = 0 #AB人数
    sab_ratio70 = 0 #AB率

    #体育健康 health
    ht_sco = 0 #语文总分 score
    ht_aver = 0 # 平均分 total average
    ht_sco70 = 0 #人数前70%总分
    ht_aver70 = 0 #人数前70%平均分

    ha_stu = 0 #A人数
    ha_ratio = 0 #A率

    hab_stu = 0 #AB人数
    hab_ratio = 0 #AB率


    hde_stu = 0 #AB人数
    hde_ratio = 0 #AB率

    hab_stu70 = 0 #AB人数
    hab_ratio70 = 0 #AB率

    # for sname in lclass:
    #     sheet = workbook[sname]

    for row in sheet.iter_rows(min_row=3):
        t_sco = round(t_sco, 1) + row[4].value

        if row[5].value == 'A':
            a_stu += 1

        if row[5].value == 'B':
            b_stu += 1

        if row[5].value == 'D':
            d_stu += 1

        if row[5].value == 'E':
            e_stu += 1

    for row in sheet.iter_rows(min_row=3, max_row=t_stu70+2):
        t_sco70 = round(t_sco, 1) + row[4].value

        if row[5].value == 'A':
            a_stu70 += 1

        if row[5].value == 'B':
            b_stu70 += 1


    t_aver = round(t_sco/t_stu, 1)
    t_aver70 = round(t_sco70/t_stu70, 1)
    a_ratio = round(a_stu/t_stu, 2)

    ab_stu = a_stu+b_stu
    ab_ratio = round(ab_stu/t_stu, 2)

    de_stu = d_stu + e_stu
    de_ratio = round(de_stu/t_stu, 2)

    ab_stu70 = a_stu70 + b_stu70
    ab_ratio70 = round(ab_stu70/t_stu, 2)

    fin_list = [
        "",t_stu,"","",
        t_aver,"",t_stu70,t_aver70,"",
        a_stu,a_ratio,"",ab_stu,ab_ratio,"",de_stu,de_ratio,"",
        ab_stu70,ab_ratio70,""
        ]

    print(fin_list)

book_name = "every.xlsx";
sheet_name = '成绩';

#filter_excel(book_name, sheet_name)
cal_excel(book_name)
