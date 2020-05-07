# -*- coding:utf-8 -*-


import unittest
from use_test_demo import Web
import HTMLTestRunner
import time

now = time.strftime('%Y%m%d %H%M%S',time.localtime())

suite = unittest.TestSuite()
test_dir = './'
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='use_test*.py')
suite.addTests(discover)
runner = unittest.TextTestRunner()
reportFile = now + '_testResult.html'
with open(reportFile,'wb') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='针对日志系统注册登陆的测试',tester='bean-jun')
    runner.run(suite)