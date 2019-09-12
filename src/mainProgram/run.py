# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


import unittest
from src.common.BeautifulReport import BeautifulReport
# from BeautifulReport import BeautifulReport
import os, time, json
from src.common.dingDing import send_link
from time import sleep
import socket

sep = os.sep
root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)


def get_project_robot_URL(projectName=None):
	json_path = f"{root_path}{sep}data{sep}jsonFiles{sep}{projectName}.json"
	# 读取json数据文件中的内容
	with open(json_path, "r", encoding="utf-8") as j:
		json_data = json.load(j)
	return json_data
	
	
def start(cases_dir=None):

	# 判断是否有指定用例文件夹
	if cases_dir:
		project_dir = cases_dir  # test_ddsf
		project_name = project_dir[-4:]   # ddsf
		robot_url = get_project_robot_URL(project_name)[project_name]["robot_data"]["robot_url"]
		suites_dir = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % sep)) + sep + sep.join(['src', 'testProject',
		                                                                                          f'{project_dir}'])
		suite = unittest.defaultTestLoader.discover(start_dir=suites_dir, pattern='*login1_test.py')
	else:
		# 这里需要补充测试组机器人URL
		robot_url = None
		suites_dir = root_path + f'{sep}src{sep}testProject'
		suite = unittest.defaultTestLoader.discover(start_dir=suites_dir)
		
	reportDirName = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % sep)) + sep + 'output' + sep + 'report' + sep

	now = time.strftime("%Y_%m_%d-%H_%M_%S")

	while True:
		report_dir = 'report_{_now}'.format(_now=now)
		reportDir = reportDirName + report_dir
		try:
			os.makedirs(reportDir)
			break
		except OSError as e:
			if e.errno != os.errno.EEXIST:
				raise
			# time.sleep might help here
			pass

	reportFileName = now + '_result.html'

	with open(reportDir + sep + reportFileName, "wb"):
		beaRep = BeautifulReport(suite)
		res = beaRep.report(filename=reportFileName, description='多多商服接口自动化测试', report_dir=reportDir)
	# return res
	sleep(5)
	# 测试报告所在的文件夹
	res_path = root_path + f'{sep}output{sep}report{sep}'
	# 切换到日志文件夹所在目录
	os.chdir(res_path)
	# 启动该目录下的服务
	report_dir = 'report_{_now}'.format(_now=now)  # report_2019_09_11-21_02_55
	result_url = "http://" + ip + f':9999{sep}{report_dir}{sep}{reportFileName}'
	print(f'{sep}{reportFileName}')  # /2019_09_11-19_42_30_result.html
	print(result_url)
	send_link(robot_url, result_url, '多多商服接口自动化测试')
	return res

if __name__ == '__main__':
	# start("https://oapi.dingtalk.com/robot/send?access_token=c41f688c4e87a482459697c9675d7a12dc6ebfbec9c242ccf2b498bcece2644a")
	# get_project_robot_URL()
	start('test_ddsf')
	# print(os.getcwd())

	
# TODO  根据不同项目启动
