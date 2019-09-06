# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-12


import unittest
from src.common.BeautifulReport import BeautifulReport
# from BeautifulReport import BeautifulReport
import os, time


def start():

	tmp = os.sep
	
	suites_dir = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % tmp)) + tmp + tmp.join(['src', 'testProject',
	                                                                                          'test_ddsf'])
	suite = unittest.defaultTestLoader.discover(start_dir=suites_dir, pattern='*1_test.py')
	reportDirName = os.path.abspath(os.path.join(os.getcwd(), "..%s.." % tmp)) + tmp + 'output' + tmp + 'report' + tmp
	
	now = time.strftime("%Y_%m_%d-%H_%M_%S")
	
	while True:
		reportDir = reportDirName + 'report_{_now}'.format(_now=now)
		try:
			os.makedirs(reportDir)
			break
		except OSError as e:
			if e.errno != os.errno.EEXIST:
				raise
			# time.sleep might help here
			pass
		
	reportFileName = now + '_result.html'
	
	with open(reportDir + tmp + reportFileName, "wb"):
		beaRep = BeautifulReport(suite)
		res = beaRep.report(filename=reportFileName, description='多多商服接口自动化测试', report_dir=reportDir)
	return res

if __name__ == '__main__':
	start()