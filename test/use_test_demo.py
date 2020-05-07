# -*- coding:utf-8 -*-


import unittest
from selenium import webdriver
import time 
import parameterized
import HTMLTestRunner


driver = None
data = []
with open('./demo_test_data.txt','r') as f:
    for i in f:
        t = i.split()
        data.append(t)


# 定义测试类
class Web(unittest.TestCase):
    '''简易网页测试'''
    @classmethod
    def setUpClass(cls):
        global driver
        driver = webdriver.Chrome()
    
    @classmethod
    def tearDownClass(cls):
        global driver
        driver.quit()
    
    def setUp(self):
        driver.get('http://beanjun.pythonanywhere.com/')
    
    def tearDown(self):
        driver.find_element_by_link_text('注销').click()
    
    @parameterized.parameterized.expand(data)
    def test2Register(self,username,password):
        # 注册账号
        driver.find_element_by_link_text('注册').click()
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password1').send_keys(password)
        driver.find_element_by_name('password2').send_keys(password)
        driver.find_element_by_name('submit').click()
        tag_text = driver.find_element_by_xpath('//h2').text
        text = '创建自己的学习日志，并列出您正在学习的主题。'
        assert tag_text == text, '实际值:'+ tag_text
        
    @parameterized.parameterized.expand(data)      
    def test3Login(self,username,password):
        # 登陆账号
        driver.find_element_by_link_text('登录').click()
        driver.find_element_by_name('username').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('submit').click()
        tag_text = driver.find_element_by_xpath('//*[@id="navbar"]/ul[2]/li[1]/a').text
        text = 'Hello, '+username+'.'
        assert tag_text == text
    

if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)