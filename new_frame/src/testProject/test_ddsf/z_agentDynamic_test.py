# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-18

import unittest
import os
import inspect
from src.common.read_data import ReadData
import ddt
import sys
from src.common.runTest import RunTest
import requests


count = 0


@ddt.ddt
class AgentDynamicTest(RunTest):
	"""经纪动态模块"""
	
	# 通过文件名夹获取project参数的值
	project = os.path.dirname(__file__)[-4:]
	a = ReadData(project)
	
	# 通过类名获取fieldname的值
	fieldname = sys._getframe().f_code.co_name[:-4]
	
	@classmethod
	def setUpClass(cls):
		cls.env_num = cls.a.get_num_name("环境")
		cls.api_name = cls.a.get_num_name("接口名称")
		cls.method_num = cls.a.get_num_name("请求方法")
		cls.headers_num = cls.a.get_num_name("请求头")
		cls.para_num = cls.a.get_num_name("请求参数")
		cls.desc_num = cls.a.get_num_name("用例描述")
		cls.data_num = cls.a.get_num_name("请求体")
		cls.expect_num = cls.a.get_num_name("预期结果")
		cls.isSkip_num = cls.a.get_num_name("是否跳过该用例")
		cls.relateData_num = cls.a.get_num_name("接口关联参数")
	
	def setUp(self):
		globals()['count'] += 1
		self.logger.debug("...start %s case %s...".center(80, '#') % (self.fieldname, count))
	
	def tearDown(self):
		self.logger.debug("...end %s case %s...".center(80, '#') % (self.fieldname, count))
	
	@ddt.data(*a.get_data_by_api(fieldname, "AgentDynamic"))
	def test_AgentDynamic(self, value):
		"""经纪动态列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.isSkip_num, self.method_num, url, self.para_num, self.data_num, self.api_name,
		                    self.desc_num, self.relateData_num, value, headers=value[self.headers_num])
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		self.logger.debug(f"响应结果         :{res}")
		self.logger.debug(f"预期结果         :{value[self.expect_num]}")
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])
		data = value[self.data_num]
		if res["data"]["pageInfo"]["total"] >= data["pageSize"]:
			self.assertEqual(len(res["data"]["pageData"]), data["pageSize"])
		else:
			self.assertEqual(len(res["data"]["pageData"]), res["data"]["pageInfo"]["total"])
		# print(res["data"]["pageInfo"]["total"])
	
	@ddt.data(*a.get_data_by_api(fieldname, "DynamicDetail"))
	def test_DynamicDetail(self, value):
		"""经纪动态-详情"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.isSkip_num, self.method_num, url, self.para_num, self.data_num, self.api_name,
		                    self.desc_num, self.relateData_num, value, headers=value[self.headers_num])
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		self.logger.debug(f"响应结果         :{res}")
		self.logger.debug(f"预期结果         :{value[self.expect_num]}")
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])
		self.assertEqual(res["data"]["customerName"], value[self.expect_num]["data"]["customerName"])
		
	@ddt.data(*a.get_data_by_api(fieldname, "StoreList"))
	def test_StoreList(self, value):
		"""经纪动态-最近拜访门店列表"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.isSkip_num, self.method_num, url, self.para_num, self.data_num, self.api_name,
		                    self.desc_num, self.relateData_num, value, headers=value[self.headers_num])
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		self.logger.debug(f"响应结果         :{res}")
		self.logger.debug(f"预期结果         :{value[self.expect_num]}")
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])
		data = value[self.data_num]
		if res["data"]["totalRecord"] >= data[0]["pageSize"]:
			self.assertEqual(len(res["data"]["results"]), data[0]["pageSize"])
		else:
			self.assertEqual(len(res["data"]["results"]), res["data"]["totalRecord"])
		# print(res["data"]["totalRecord"])
		
	@ddt.data(*a.get_data_by_api(fieldname, "StoreByStoreId"))
	def test_StoreByStoreId(self, value):
		"""经纪动态-门店详情"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.isSkip_num, self.method_num, url, self.para_num, self.data_num, self.api_name,
		                    self.desc_num, self.relateData_num, value, headers=value[self.headers_num])
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		self.logger.debug(f"响应结果         :{res}")
		self.logger.debug(f"预期结果         :{value[self.expect_num]}")
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])
		self.assertEqual(res["data"]["storeId"], value[self.expect_num]["data"]["storeId"])
		
	@ddt.data(*a.get_data_by_api(fieldname, "StoreMessage"))
	def test_StoreMessage(self, value):
		"""经纪动态-门店拜访选项字段"""
		# 通过函数名获取apiName参数的值
		self.apiName = (inspect.stack()[0][3])[5:]
		env = value[self.env_num]
		url = self.a.get_domains()[env] + self.a.get_apiPath(self.fieldname, self.apiName)
		result = self.start(self.isSkip_num, self.method_num, url, self.para_num, self.data_num, self.api_name,
		                    self.desc_num, self.relateData_num, value, headers=value[self.headers_num])
		# result = requests.post(url=url, json=value[self.data_num])
		res = result.json()
		self.logger.debug(f"响应结果         :{res}")
		self.logger.debug(f"预期结果         :{value[self.expect_num]}")
		# print(res["code"])
		self.assertEqual(res["code"], value[self.expect_num]["code"])
		self.assertEqual(res["data"]["storeId"], value[self.expect_num]["data"]["storeId"])