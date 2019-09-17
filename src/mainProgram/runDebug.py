# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-02


import unittest
import HTMLTestReportCN
import os
from BeautifulReport import BeautifulReport
import time


tmp = os.sep


if __name__ == '__main__':
	# # 方式1：控制单条用例执行
	# suite = unittest.TestSuite()
	# # suite.addTest(a_login_test.LoginTest('test_ByPassword'))
	# # suite.addTest(b_home_test.HomeTest('test_HomeInfo'))
	# suite.addTest(c_store_test.StoreTest('test_getOrgStore'))
	# HTMLTestReportCN.HTMLTestRunner(stream=open(os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	#                                             'output/report' + tmp + 'report.html', 'wb'),
	#                                 title='多多商服接口自动化测试报告', description=TemplateTeseCase.env + "环境测试报告",
	#                                 tester='Bo_lin Chen').run(suite)
	
	# 方式2：通过case文件名指定接口测试

	suite = unittest.defaultTestLoader.discover(start_dir=os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	                                                      'src/testProject/test_ddsf', pattern='z_agentDynamic_test.py')
	# suite2 = unittest.defaultTestLoader.discover(start_dir=os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	#                                                       'src/testProject/test_ddsf', pattern='home_test.py')
	# print(suite)
	# suite = suite.addTests(suite2)
	HTMLTestReportCN.HTMLTestRunner(stream=open(os.path.abspath(os.path.join(os.getcwd(), "../..")) + tmp +
	                                            'output/report' + tmp + 'report.html', 'wb'),
	                                title='多多商服接口自动化测试报告', description="正式环境测试报告",
	                                tester='Bo_lin Chen').run(suite)
	# ###################################################################################################################
	# suite = unittest.defaultTestLoader.discover(start_dir=os._path.abspath(os.path.join(os.getcwd(), "..%s.." % tmp)) +
	#                                                       tmp + 'src/testProject/test_ddsf', pattern='*test.py')
	# reportName = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % tmp)) + tmp + 'output' + tmp + 'report' + tmp
	# print(reportName)
	#
	# now = time.strftime("%Y_%m_%d-%H_%M_%S")
	# # #
	# # reportDir = './report/' + 'report_{_now}'.format(_now=now)
	# while True:
	# 	reportDir = reportName + 'report_{_now}'.format(_now=now)
	# 	try:
	# 		os.makedirs(reportDir)
	# 		# print(reportDir)
	# 		break
	# 	except OSError as e:
	# 		if e.errno != os.errno.EEXIST:
	# 			raise
	# 		# time.sleep might help here
	# 		pass
	# # print(os.path.abspath(reportDir))  # /Users/wawa/Desktop/new_frame/out/report/report_2019_08_12-01_04_49
	# reportName1 = now + '_result.html'
	# # print(reportName1)
	# #
	# # with open(reportName1, "wb") as fp:
	# # 	beaRep = BeautifulReport(suite)
	# # 	res = beaRep.report(filename=reportName1, description='多多商服接口自动化测试', report_dir=reportDir)
	# # # print(os.path.abspath(reportName))
	#
	# with open(reportDir + tmp + reportName1, "wb") as fp:
	# 	beaRep = BeautifulReport(suite)
	# 	res = beaRep.report(filename=reportName1, description='多多商服接口自动化测试', report_dir=reportDir)
	# # print(os.path.abspath(reportName))