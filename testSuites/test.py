# coding=utf-8
from HTMLTestRunner_cn import HTMLTestRunner
# import HTMLTestRunner
import os
import unittest
import time
import sys
sys.path.append(os.path.dirname(os.path.abspath('.')))

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/testReport/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

# 构建suite
suite = unittest.TestLoader().discover("testModule")
# suite = unittest.TestSuite()
# suite.addTest()

if __name__ =='__main__':

    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner(
        title="自动化测试报告",
        description="",
        tester="少年",
        stream=fp,
        verbosity=2, retry=0, save_last_try=True)
    # 开始执行测试套件
    runner.run(suite)