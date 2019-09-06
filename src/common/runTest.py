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


# 定义断言函数
def checkOut(res, exp):
	for _key in exp:
		value = [_key, exp[_key]]
		check = jsonpath(res, expr=f"$..{value[0]}")
		if check[0] == value[1] and check:
			pass
		else:
			# print(f"断言失败！！！响应体中{_key}该字段的值为:{check[0]}，而预期结果为:{exp[_key]}")
			return False
	# print("断言成功！")
	return True


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
	
	def start(self, isSkip_num, apiName_num,  url, method_num, headers_num, para_num, data_num, desc_num, isRelate_num,
	          expect_num, *args, **kw):
		"""
		用例运行主入口
		:param isSkip_num:      是否跳过列数来判断该用例是否跳过执行
		:param apiName_num:     接口名称所在列数，获得接口名称
		:param url:             请求地址
		:param method_num:      请求方法所在列数
		:param headers_num      请求头所在列数
		:param para_num:        接口请求参数所在列数
		:param data_num:        接口请求体所在列数
		:param desc_num:        接口描述所在列数
		:param isRelate_num:    接口是否存在依赖参数所在列
		:param args:            从excle表中获取到的每条用例的测试数据
		:return:                API调用返回结果
		"""

		isSkip = args[0][isSkip_num]
		api_name = args[0][apiName_num]
		method = args[0][method_num]
		self.headers = args[0][headers_num]
		params = args[0][para_num]
		self.body = args[0][data_num]
		self.desc = args[0][desc_num]
		isRelate = args[0][isRelate_num]
		self.expect = args[0][expect_num]
		time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		
		try:
			# log日志中写入用例执行之前的一些相关数据
			self.logger.debug(f"用例名称         :{api_name}")
			self.logger.debug(f"用例描述         :{self.desc}")
			self.logger.debug(f"用例执行时间      :{time_str}")
			self.logger.debug(' 请求信息 '.center(80, '-'))
			self.logger.debug(f"用例请求方法      :{method}")
			self.logger.debug(f"接口地址         :{url}")
			self.logger.debug(f"请求参数         :{params}")
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
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求体           :{self.body}")
			response = self.method.run_main(url, method, self.headers, params, self.body, **kw)
			# write_relate_json(data=res, relate_config=relateData)
			try:
				res = response.json()
				self.logger.debug(f"响应结果         :{res}")
				self.logger.debug(f"预期结果         :{self.expect}")
			except Exception as err:
				self.logger.error(str(err))
			else:
				for _dict in relateData:
					for _key in _dict:
						a = [_key, _dict[_key]]
						relate_value = jsonpath(res, expr=f"$..{a[0]}")
						if relate_value:
							# 这里如果 relate_value 存在的话类型其实是列表，所以取值使用需要注意
							sss[a[1]] = relate_value[0]
							self.logger.info(f"依赖数据缓存成功    :{a[0]}-->{a[1]}, 数据值为:{relate_value[0]}")
						else:
							self.logger.info("返回数据汇中指定的关联数据获取失败！")
			# print(sss)
			return res
		# 如果该接口关联类型只是关联输入
		elif isRelate and isRelate["relateType"] == "relateIn":
			# 获取存放的所有关联数据(这里其实数据不多，所以暂时统一存放在一个dict中)
			# 将headers/请求体中的关联参数赋值激活
			# 声明参数化的字段使用 两个#号夹住的写法，这里字段名称只能使用字母和数字--\w
			re_str = '#\w+#'
			# 使用正则获取headers中参数化的字段列表
			self.headers = str(self.headers)
			self.body = str(self.body)
			self.expect = str(self.expect)
			re_list_header = re.findall(re_str, self.headers)
			# 使用正则获取请求体中参数化的字段列表
			re_list_body = re.findall(re_str, self.body)
			# 使用正则获取预期结果(断言)中参数化的字段列表
			re_list_expect = re.findall(re_str, self.expect)
			# 对headers中参数化的字段进行激活赋值
			for m in re_list_header:
				self.headers = self.headers.replace(m, "f'{data[\"%s\"]}'" % (m[1:-1]))
			# 对请求体中参数化的字段进行激活赋值
			for n in re_list_body:
				self.body = self.body.replace(n, "f'{data[\"%s\"]}'" % (n[1:-1]))
			# 对预期结果中参数化的字段进行激活赋值
			for o in re_list_expect:
				self.expect = self.expect.replace(o, "f'{data[\"%s\"]}'" % (o[1:-1]))
			data = sss
			# 对激活后的 headers/请求体/预期结果做类型转换
			self.headers = eval(self.headers)
			self.body = eval(self.body)
			self.expect = eval(self.expect)
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求体           :{self.body}")
			response = self.method.run_main(url, method,  self.headers, params, self.body, **kw)
			try:
				res = response.json()
				self.logger.debug(f"响应结果         :{res}")
				self.logger.debug(f"预期结果         :{self.expect}")
			except Exception as err:
				self.logger.error(str(err))
			# print(data)
			return res
		elif isRelate and isRelate["relateType"] == "all":
			
			re_str = '#\w+#'
			self.headers = str(self.headers)
			self.body = str(self.body)
			self.expect = str(self.expect)
			# 使用正则获取headers中参数化的字段列表
			re_list_header = re.findall(re_str, self.headers)
			# 使用正则获取请求体中参数化的字段列表
			re_list_body = re.findall(re_str, self.body)
			# 使用正则获取预期结果(断言)中参数化的字段列表
			re_list_expect = re.findall(re_str, self.expect)
			# 对headers中参数化的字段进行激活赋值
			for m in re_list_header:
				self.headers = self.headers.replace(m, "f'{data[\"%s\"]}'" % (m[1:-1]))
			# 对请求体中参数化的字段进行激活赋值
			for n in re_list_body:
				self.body = self.body.replace(n, "f'{data[\"%s\"]}'" % (n[1:-1]))
			# 对预期结果中参数化的字段进行激活赋值
			for o in re_list_expect:
				self.expect = self.expect.replace(o, "f'{data[\"%s\"]}'" % (o[1:-1]))
			data = sss
			# 对激活后的 headers/请求体/预期结果做类型转换
			self.headers = eval(self.headers)
			self.body = eval(self.body)
			self.expect = eval(self.expect)
			self.logger.debug(f"header          :{self.headers}")
			self.logger.debug(f"请求体           :{self.body}")
			relateData = isRelate["relateData"]
			response = self.method.run_main(url, method, self.headers, params, self.body, **kw)
			try:
				res = response.json()
				self.logger.debug(f"响应结果         :{res}")
				self.logger.debug(f"预期结果         :{self.expect}")
			except Exception as err:
				self.logger.error(str(err))
			else:
				for _dict in relateData:
					for _key in _dict:
						a = [_key, _dict[_key]]
						relate_value = jsonpath(res, expr=f"$..{a[0]}")
						if relate_value:
							# 这里如果 relate_value 存在的话类型其实是列表，所以取值使用需要注意
							sss[a[1]] = relate_value[0]
							self.logger.info(f"依赖数据缓存成功:{a[0]}-->{a[1]}, 数据值为:{relate_value[0]}")
						else:
							self.logger.info("返回数据汇中指定的关联数据获取失败！")
			# print(sss)
			return res
		else:
			self.logger.debug(f"请求体           :{self.body}")
			response = self.method.run_main(url, method, self.headers, params, self.body, **kw)
			try:
				res = response.json()
				self.logger.debug(f"响应结果         :{res}")
				self.logger.debug(f"预期结果         :{self.expect}")
			except Exception as err:
				self.logger.error(str(err))
			return res