# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


"""基础类，封装requests请求方法"""

import requests


class MethodException(Exception):
	pass


class RunMethod(MethodException):
	
	headers_default = {"content-type": "application/json"}
	
	def run_main(self, url=None, method=None, headers=headers_default, para=None, data=None, **kw):
		
		"""
        封装常用的7种http请求方法
        :param method:        请求方法，从而获取请求方法 如 GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD
        :param url:           请求url
        :param headers:       请求头，从而获取到请求头， 默认为 application/json
        :param para:          请求参数，从而获取到请求参数，默认 None
        :param data:          请求体数据，从而获取到请求体参数，默认 None
        :param kw:            其他参数
        :return:        Response object，type requests.Response
        """
		
		try:
			if method:
				if method.lower() == "get":
					res = requests.get(url, params=para, **kw)
				elif method.lower() == "post":
					if headers["content-type"] == "application/json":
						res = requests.post(url, params=para, json=data, **kw)
					else:
						res = requests.post(url, params=para, data=data, **kw)
				elif method.lower() == 'put':
					res = requests.put(url, params=para, data=data, **kw)
				elif method.lower() == 'patch':
					res = requests.patch(url, params=para, data=data, **kw)
				elif method.lower() == 'delete':
					res = requests.delete(url, params=para, **kw)
				elif method.lower() == 'head':
					res = requests.head(url, params=para, **kw)
				elif method.lower() == 'options':
					res = requests.options(url, params=para, **kw)
				else:
					print("Do Not Support Http Method!Please check the args of requests")
					raise MethodException
				return res
		except Exception as err:
			raise "接口请求数据获取失败！" + str(err)