# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-20

# 初始化字典
ini_dict = {'a': 'akshat', 'b': 'bhuvan', 'c': 'chandan'}
a = {"name": "kobe"}

# 将字典拆分为键和值的列表
keys = ini_dict.keys()
values = ini_dict.values()

# a = zip(keys,values)
# print(list(a))
for i in a:
	b = [i, a[i]]
	print(b[1])