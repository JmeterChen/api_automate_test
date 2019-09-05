# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-20


import os
import json
from jsonpath import jsonpath
# import requests


grandpa_path = os.path.abspath(os.path.join(__file__, "../../.."))
json_str = r"%s/data/relateData.json" % grandpa_path


def write_relate_json(path=json_str, data=None, relate_config=None):
	src = {}
	data = data.json()
	for _dict in relate_config:
		for _key in _dict:
			a = [_key, _dict[_key]]
			relate_value = jsonpath(data, expr=f"$..{a[0]}")
			if relate_value:
				# 这里如果 relate_value存在，类型为列表，所以取值使用需要注意
				src[a[1]] = relate_value[0]
			else:
				print("返回数据中指定的关联数据获取失败！")
	with open(path, 'a', encoding="utf-8") as f:
		# 将依赖数据以 接口名称(被依赖接口)-->key-->value 的形式覆盖写入指定json文件
		json.dump(src, f, indent=4)


def read_relate_json(path=json_str) -> dict:
	# 打开获得依赖数据的json文件并以字典格式返回
	with open(path, "r", encoding="utf-8") as f:
		# data = json.loads(f.read())
		data = json.load(f)
		return data
	
	
def write_relate_DATA(data=None, relate_config=None):
	src = {}
	data = data.json()
	for _dict in relate_config:
		for _key in _dict:
			a = [_key, _dict[_key]]
			relate_value = jsonpath(data, expr=f"$..{a[0]}")
			if relate_value:
				# 这里如果 relate_value存在，类型为列表，所以取值使用需要注意
				src[a[1]] = relate_value[0]
			else:
				print("返回数据中指定的关联数据获取失败！")
	return src

if __name__ == '__main__':
# 	# data1 = {"name": "kobe"}
# 	# wirte_to_json(data=data1)
# 	url = 'https://as-web.fangdd.com/data/fetchDynamicDetail'
# 	header = {"restful": '{"recordId": "421050"}'}
# 	# header = json.dumps(header)
# 	read_relate_json()

	data = read_relate_json()
	print(data)