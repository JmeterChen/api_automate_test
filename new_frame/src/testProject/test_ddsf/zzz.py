# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08

import sys
import requests
import json
import os
from jsonpath import jsonpath


# class HTest:
#
# 	a = (sys._getframe().f_code.co_name)[:-4]
# 	print(a)
#
#
# b = HTest()

# if __name__ == '__main__':
#
# 	url = 'https://as-web.fangdd.com/data/fetchDynamicDetail'
# 	header = {"restful": '{"recordId": "421050"}'}
# 	# header = json.dumps(header)
#
# 	res = requests.get(url=url, headers=header)
# 	# res_dict = json.loads(res.text)
# 	# res_dict = json.loads(res.json())
# 	res_dict = res.json()
	# print(res_dict)
	# # id_list = jsonpath(res_dict, expr="$..id")
	# id_list = jsonpath(res_dict, expr="$..*")
	# print(id_list)
	# print()
	
	
# userID = 24

# _data = {"userID": '23', "name": 'kobe'}
#
# a = {"staffID": int(f'{_data["userID"]}')}
# b = {"name": f'{_data["name"]}', "message": [{"num": 24, "teams": "Lake", "cardID": int(f'{_data["userID"]}')}],
#      "staffID": f'{_data["name"]}'}
# c = [{"name": f'{_data["name"]}', "message": [{"num": 24, "teams": "Lake", "cardID": int(f'{_data["userID"]}')}],
#      "staffID": f'{_data["name"]}'}]
# # print(a)
# # print(b)
# print(c)

if __name__ == '__main__':
     
     # data = {
     #     "ID": 6520137
     # }
     # # # body = [{"staffId":f'{data["ID"]}'}, {"opId": f'{data["ID"]}', "systemSource":"DD_COMMERCIAL"}]
     # # # print(body)
     # # a = '{"userId":f\'{data["ID"]}\'}'
     # #
     # # b = eval(a)
     # # print(b)
     #
     # b = [{"staffId":f'{data["ID"]}'},{"opId":f'{data["ID"]}',"systemSource":"DD_COMMERCIAL"}]
     # c = {"userId":f'{data["ID"]}'}
     # print(b)
     # print(c)
     
     a = "dfgfgdfbjgbdfjbnone{'dfbdjbgfalsehj'dfgf[true]dgbffgh}"
     print(a)
     a2 = a.replace("none", "None")
     print(a2)