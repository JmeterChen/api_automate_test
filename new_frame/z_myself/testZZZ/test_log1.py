# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-16


import logging

# 创建一个日志器logger并设置其日志级别为DEBUG
logger = logging.getLogger('simple_logger')
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename="app.log", level=logging.DEBUG)

# 日志输出
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')