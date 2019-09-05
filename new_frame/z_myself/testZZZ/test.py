# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-03


import re

# def aaaa(**kwargs):
# 	if kwargs.get("kobe"):
# 		print(kwargs["kobe"])
# 	else:
# 		print(2222)
#
#
# aaaa(kobe1='name')

# a = 'fghgfh#{ID}#fgh#{fg}#45'
a = '[{"staffId":#ID#},{"opId":#ID#,"systemSource":"DD_COMMERCIAL"}]'
a_re = re.findall("#\w+#", a)

print(a_re)   # #ID#

# # b = re.sub("#.+#", "f'{data['%s']}'" %(a_re[1:-1]), a)
# # print(b)
#
for i in a_re:
	a = a.replace(i, "f'{data[\"%s\"]}'" % (i[1:-1]))
	

print(a)