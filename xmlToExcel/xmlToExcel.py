#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
author: tfss
e-mail: 1255791430@qq.com
'''

import xmltodict
import xlwt
from xlwt import Workbook
# from datetime import datetime

# 实例化一个Workbook()对象(即excel文件)
wbk = xlwt.Workbook()
# 新建一个名为Sheet1的excel sheet。此处的cell_overwrite_ok =True是为了能对同一个单元格重复操作。
sheet = wbk.add_sheet('Sheet1',cell_overwrite_ok=True)
book = Workbook(encoding='utf-8')
sheet1 = book.add_sheet('Sheet 1')


with open('130000.xml',encoding="UTF-8") as fd:
    doc = xmltodict.parse(fd.read())

system=doc['Result']['System']
print(system['Region'],system['PublicOrg'],system['Updatetime'],system['CityTitle'],system['PointerTitle'])
citys = doc['Result']['Citys']['City']

# 文件头
for i, key in enumerate(['Name', 'DataTime', 'AQI', 'Level', 'LevelIndex', 'MaxPoll', 'Color', 'Intro', 'Tips']):
    sheet1.write(0, i, key)

# 文件内容
for idx,city in enumerate(citys):

    print("--------------->",city['Name'], city['DataTime'], city['AQI'],city['Level'],city['LevelIndex'],city['MaxPoll'],city['Color'],city['Intro'],city['Tips'])

    sheet1.write(idx+1, 0, city['Name'])
    sheet1.write(idx+1, 1, city['DataTime'])
    sheet1.write(idx+1, 2, city['AQI'])
    sheet1.write(idx+1, 3, city['Level'])
    sheet1.write(idx+1, 4, city['LevelIndex'])
    sheet1.write(idx+1, 5, city['MaxPoll'])
    sheet1.write(idx+1, 6, city['Color'])
    sheet1.write(idx+1, 7, city['Intro'])
    sheet1.write(idx+1, 8, city['Tips'])


    pointers = city['Pointers']['Pointer']
    for pointer in pointers:
        print(pointer['Name'], pointer['DataTime'], pointer['AQI'],pointer['Level'],pointer['LevelIndex'],pointer['MaxPoll'],pointer['Color'],pointer['Intro'],pointer['Tips'],pointer['CLng'],pointer['CLat'])

book.save('simpleExcel.xls')