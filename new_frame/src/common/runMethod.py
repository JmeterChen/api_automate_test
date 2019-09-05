# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


"""基础类，封装requests请求方法"""

import requests


class MethodException(Exception):
	pass


class RunMethod(MethodException):
	
	def run_main(self, method_num=None, url=None, para_num=None, body_num=None, *args, **kw):
		"""
        封装常用的7种http请求方法
        :param method_num: 请求方法列数，从而获取请求方法 如 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD
        :param url:     请求url
        # :param header_num: 请求头列数， 从而获取到请求头
        :param para_num:    请求参数列数，从而获取到请求参数，默认 None
        :param body_num:  请求数据列数，从而获取到请求体参数，默认 None
        :param kw:      其他参数
        :return:        Response object，type requests.Response
        """
		
		try:
			method = args[0][method_num]
			para = args[0][para_num]
			data = args[0][body_num]
			# print(method, data)
			
			if method:
				if method.lower() == "get":
					res = requests.get(url, params=para, **kw)
				elif method.lower() == "post":
					if kw.get("json"):
						# print(kw.get("json"))
						res = requests.post(url, data=para, **kw)
					else:
						res = requests.post(url,  data=para, json=data, **kw)
				elif method.lower() == 'put':
					res = requests.put(url, data=data, **kw)
				elif method.lower() == 'patch':
					res = requests.patch(url, data=data, **kw)
				elif method.lower() == 'delete':
					res = requests.delete(url, **kw)
				elif method.lower() == 'head':
					res = requests.head(url, **kw)
				elif method.lower() == 'options':
					res = requests.options(url, **kw)
				else:
					print("Do Not Support Http Method!Please check the args of requests")
					raise MethodException
				return res
			elif para:
				return para
			elif data:
				return data
		except Exception as err:
			raise "接口请求数据获取失败！" + str(err)