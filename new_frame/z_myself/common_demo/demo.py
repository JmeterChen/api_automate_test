# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-02

import os

a = ["环境", "模块名", "接口名称", "请求方法", "请求头", "请求参数", "请求体", "预期结果", "用例名称"]

# print(a.__contains__(11))
#
# file_name = os.path.split(__file__)[-1]
# file_name_without_suffix = os.path.splitext(file_name)
# print(file_name_without_suffix[0])


b = ['环境', '模块名', '接口名称', '请求头', '请求参数', '用例名称', '请求体', '预期结果', '测试结果']

for i in a:
	if not b.__contains__(i):
		print("b列表中缺乏 %s, 请在b中补全相关数据！" % i)
	else:
		pass

