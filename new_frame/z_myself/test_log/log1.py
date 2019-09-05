# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-01

import logging

# 通过下面的方式进行简单配置输出方式与日志级别
logging.basicConfig(filename='log1.log', level=logging.DEBUG)

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')