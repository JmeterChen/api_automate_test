# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-11


def get_data_by_api(data, data_key):
	list_data = []
	for i in range(len(data)):
		if data[i][0] == data_key:
			list_data.append(data[i])
	return list_data