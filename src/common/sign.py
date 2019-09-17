# -*- coding=utf-8 -*-
# Author: BoLin Chen
# @Date : 2019-09-14


from jpype import *
import jpype
import os
import sys

# 解决在linux下执行该程序路径报错问题
sep = os.sep
root_path = os.path.abspath(os.path.join(__file__, f"..{sep}..{sep}.."))
sys.path.append(root_path)


class SignKey:
    def __init__(self, req):
        self.req = req

    def sign(self):
        jar_path = f"{root_path}{sep}src{sep}common{sep}fdd-1.1-SNAPSHOT-jar-with-dependencies.jar"
        if not jpype.isJVMStarted():
            # startJVM：本地调试使用第一个，提交代码需要注释第一个，使用第二个绝对路径的（crontab下不识别java的默认路径）
            startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s" % jar_path)
            # startJVM (r"/usr/java/jdk1.8.0_11/jre/lib/amd64/server/libjvm.so","-ea","-Djava.class.path=%s" % jar_path)
        instance = JPackage('com').fangddd.ddsign
        key = instance.SignUtil.generateSign(self.req)
        # print(type(key))
        return str(key)
    
    # def __del__(self):
    #     jpype.shutdownJVM()  # 最后关闭jvm


if __name__ == '__main__':
    str1 = '1568603350103' + 'POST' + '/user/users/login' + '{"mobile": "17900011101", "password": "123456", "mode": 1}'
    print(str1)
    a = SignKey(str1)
    # a.sign ('111111')
    
    print(a.sign())