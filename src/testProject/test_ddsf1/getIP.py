# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-11


import socket

# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)   # 10.0.44.222