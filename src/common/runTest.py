# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


import unittest
from src.common.runMethod import RunMethod
from src.common.readLogger import ReadLogger
from jsonpath import jsonpath
import time
import re

sss = {}


class RunTest(unittest.TestCase, unittest.SkipTest):
	
	def __init__(self, methodName='runTest'):
		super(RunTest, self).__init__(methodName)
		
		# 获取logger和run_log
		read_logger = ReadLogger()
		# 获取logger容器
		self.logger = read_logger.get_logger()
		# 获取日志文件路径
		self.run_log_src = read_logger.get_run_log()
		
		# 使用自封装requests
		self.method = RunMethod()
		
		self.desc = ""     # 用例描述
		self.case_id = ""  # 用例id
		self.body = None  # 因为存在接口数据依赖原因，所以这里会单独申明body
		self.req_msg = {'request': {}, '\nresponse': {}}  # 用例基本信息
		# 后面用例编号会使用
	
	def skipTest(self, reason):
		"""
		过滤用例
		:param reason:  过滤用例原因
		:return:   unittest.SkipTest
		"""
		raise unittest.SkipTest
	
	def getCasePro(self):
		"""
		获取用例基本信息
		:return: desc
		"""
		return self.desc
	
	def start(self, isSkip_num, method_num, url, para_num, body_num, apiName_num, desc_num, isRelate_num, *args, **kw):
		"""
		用例运行主入口
		:param isSkip_num:  是否跳过列数来判断该用例是否跳过执行
		:param method_num:  请求方法所在列数
		:param url:         请求地址
		:param para_num:    接口请求参数所在列数
		:param body_num:    接口请求体所在列数
		:param desc_num:    接口描述所在列数
		:param args:        从excle表中获取到的每条用例的测试数据
		:return:            API调用返回结果
		"""
		# print(args[0])
		# print(desc_num)
		# print(args[0])
		
		self.api_name = args[0][apiName_num]
		headers = kw.get("headers")
		if headers:
			self.headers = headers
		else:
			self.headers = {}
		self.desc = args[0][desc_num]
		self.body = args[0][body_num]
		# type_body = type(self.body)
		# print(type_body)
		isSkip = args[0][isSkip_num]
		isRelate = args[0][isRelate_num]
		time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		
		try:
			# log日志中写入用例执行之前的一些相关数据
			self.logger.debug(f"用例名称         :{self.api_name}")
			self.logger.debug(f"用例描述         :{self.desc}")
			self.logger.debug(f"用例执行时间      :{time_str}")
			self.logger.debug(' 请求信息 '.center(80, '-'))
			self.logger.debug(f"用例请求方法      :{args[0][method_num]}")
			self.logger.debug(f"接口地址         :{url}")
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求参数         :{args[0][para_num]}")
		except Exception as e:
			self.logger.error('错误信息   : %s' % e)
		
		# global DATA
		global sss
		# 根据是否跳过参数判断用例是否执行
		if isSkip and isSkip != "否":
			self.skipTest('skip case')
		# 如果该接口关联类型只是关联输出
		elif isRelate and isRelate["relateType"] == "relateOut":
			relateData = isRelate["relateData"]
			self.logger.debug(f"请求体           :{self.body}")
			response = self.method.run_main(method_num, url, para_num, body_num, *args, **kw)
			# write_relate_json(data=res, relate_config=relateData)
			res = response.json()
			for _dict in relateData:
				for _key in _dict:
					a = [_key, _dict[_key]]
					relate_value = jsonpath(res, expr=f"$..{a[0]}")
					if relate_value:
						# 这里如果 relate_value 存在的话类型其实是列表，所以取值使用需要注意
						sss[a[1]] = relate_value[0]
					else:
						print("返回数据汇中指定的关联数据获取失败！")
			# print(sss)
			return response
		# 如果该接口关联类型只是关联输入
		elif isRelate and isRelate["relateType"] == "relateIn":
			# 获取存放的所有关联数据(这里其实数据不多，所以暂时统一存放在一个dict中)
			# 从json中获取依赖数据部分
			# data = read_relate_json()
			# 将请求体中的关联参数赋值激活
			
			re_str = '#\w+#'
			re_list = re.findall(re_str, self.body)
			for i in re_list:
				self.body = self.body.replace(i, "f'{data[\"%s\"]}'" % (i[1:-1]))
			data = sss
			self.body = eval(self.body)  # 这一步骤的理由是虽然从excle中的数据
			self.logger.debug(f"请求体           :{self.body}")
			response = self.method.run_main(method_num, url, para_num, body_num, *args, json=self.body)
			# print(data)
			return response
		elif isRelate and isRelate["relateType"] == "all":
			
			re_str = '#\w+#'
			re_list = re.findall(re_str, self.body)
			for i in re_list:
				self.body = self.body.replace(i, "f'{data[\"%s\"]}'" % (i[1:-1]))
			data = sss
			self.body = eval(self.body)  # 这一步骤的理由是虽然从excle中的数据
			self.logger.debug(f"请求体           :{self.body}")
			relateData = isRelate["relateData"]
			response = self.method.run_main(method_num, url, para_num, body_num, *args, json=self.body)
			res = response.json()
			for _dict in relateData:
				for _key in _dict:
					a = [_key, _dict[_key]]
					relate_value = jsonpath(res, expr=f"$..{a[0]}")
					if relate_value:
						# 这里如果 relate_value 存在的话类型其实是列表，所以取值使用需要注意
						sss[a[1]] = relate_value[0]
					else:
						print("返回数据汇中指定的关联数据获取失败！")
			# print(data)
			return response
		else:
			self.logger.debug(f"请求体           :{self.body}")
			response = self.method.run_main(method_num, url, para_num, body_num, *args, **kw)
			return response