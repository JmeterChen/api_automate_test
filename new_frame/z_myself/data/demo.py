# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-01

import xlrd
from xlutils.copy import copy


workbook = xlrd.open_workbook("FDD接口测试用例.xlsx")  # 返回数据对象

sheet_names = workbook.sheet_names()  # 获得表格中的所有页签名称列表

print(sheet_names)
# sheet_ddsf = workbook.sheet_by_name(sheet_names[0])

sheet_dict = {}
for i in range(len(sheet_names)):
	name = sheet_names[i]
	locals()[name] = workbook.sheet_by_name(sheet_names[i])
	sheet_dict[name] = locals()[name]

print(sheet_dict)

sheet_ddsf = sheet_dict["ddsf"]
# print(sheet_ddsf.nrows)  # 6行
for i in range(1, sheet_ddsf.nrows):
	print(sheet_ddsf.row_values(i))

