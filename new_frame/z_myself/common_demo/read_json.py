# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-08

import os
import json


class ReadJson:
	def __init__(self, project=None, env=None):
		
		grandpa_path = os.path.abspath(os.path.join(__file__, "../../.."))
		json_str = r"%s/data/config.json" % grandpa_path
		
		with open(json_str, 'r', encoding="utf-8") as f:
			self.data = json.load(f)
		self.env = env
		self.project = project
		self.fieldname = None
		self.apiName = None
		self.domain = self.data["url"][project]["domain"] % self.data["suffix"][env]
	
	def get_url(self, fieldname, apiName):
		self.fieldname = fieldname
		self.apiName = apiName
		path = self.data["url"][self.project][fieldname][apiName]
		url = self.domain + path
		return url
	
	def get_header(self, data_type="header_json"):
		return self.data["headers"][data_type]
	
	def get_body(self, api_name=None):
		if api_name:
			self.apiName = api_name
		else:
			self.apiName = self.apiName
		return self.data["body"][self.project][self.env][self.fieldname][self.apiName]
	
	def get_robot_data(self):
		return self.data["robot_data"][self.project]