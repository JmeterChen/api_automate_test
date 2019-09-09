# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-08-23


"""基础类，用于读取日志配置和和获取日志文件"""
import os
import logging
import logging.config


sep = os.sep


class ReadLogger:
    def __init__(self, logType=None):
        """ 读取日志配置 """
        root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 项目根路径
        # print(root_dir)
        # root_dir = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))  # 项目根路径
        # print(root_dir)
        if not logType:
            log_conf_file = 'logging.conf'  # 日志配置文件
            log_path = root_dir + sep + 'conf' + sep + log_conf_file  # 日志配置文件绝对路径
            # print(log_path)
            logging.config.fileConfig(log_path)
            self.logger = logging.getLogger('simpleExample')
            # # # 生成日志文件
            # log_src = "run.log"  # 运行时日志
        else:
            log_conf_file = f'{logType}Log.conf'  # 日志配置文件
            log_path = root_dir + sep + 'conf' + sep + log_conf_file  # 日志配置文件绝对路径
            # print(log_path)
            logging.config.fileConfig(log_path)
            self.logger = logging.getLogger(f'{logType}')
        #     # # 生成日志文件
        #     log_src = f"{logType}.log"  # 运行时日志
        #
        # self.run_log_src = root_dir + sep + f'output{sep}logs' + sep + log_src

    def get_logger(self):
        """ 获取logger容器 """
        return self.logger
    
    # def get_run_log(self):
    #     """ 获取日志文件路径 """
    #     return self.run_log_src

if __name__ == "__main__":
    read_logger = ReadLogger()
    logger = read_logger.get_logger()
    logger.debug('debug message')
