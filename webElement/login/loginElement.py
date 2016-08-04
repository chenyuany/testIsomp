#coding=utf-8
u''' 
#文件名：login
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-09-16
#模块描述：登录页面
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import Select

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement

 
class loginPage:
    #登录方式
    LOGIN_METHOD = "loginMethod"
    #用户名
    LOGIN_USERNAME = "username"
    #口令
    LOGIN_PWD = "pwd"
    #登录按钮
    LOGIN_BUTTON = "do_login"
    #系统名称
    LOGIN_SYSTEM_NAME = "systemName"
    #帮助与控件下载
    LOGIN_DOWNLOAD = "/html/body/div[2]/div[5]/a"
    #版权所有
    LOGIN_COPYRIGHT = "/html/body/div[2]/div[5]/text()[2]"
    
    def __init__(self,driver):
        #selenuim驱动
        self.driver = driver
        self.getElem = getElement(driver)
    
    #获取登录方式
    def get_login_method(self):
        #loginMethod = driver.find_element_by_id(self.LOGIN_METHOD)
        loginMethod = getElem.find_element('id',self.LOGIN_METHOD)
        
    #设定登录方式
    def set_login_method(self,driver,index): 
        try:
            loginMethod = driver.find_element_by_id(self.LOGIN_METHOD)
            Select(loginMethod).select_by_index(index)
        except Exception as e:
            print "login type error:" + str(e)
        
    #填写用户名
    def set_login_username(self,username):
        try:
            getElem = getElement(self.driver)
            name = getElem.find_element('id',loginPage().LOGIN_USERNAME)
            #name = driver.find_element_by_id(loginPage().LOGIN_USERNAME)
            name.send_keys(username)
        except Exception as e:
            print "login name error:" + str(e)
        
    #填写口令
    def set_login_pwd(self,driver,pwd):
        try:
            password = driver.find_element_by_id(self.LOGIN_PWD)
            password.send_keys(pwd)
        except Exception as e:
            print "login password error:" + str(e)
    
    #填写用户名
    def set_login_element(self,element):
        try:
            name = self.getElem.find_element('id',loginPage().LOGIN_USERNAME)
            #name = driver.find_element_by_id(loginPage().LOGIN_USERNAME)
            name.send_keys(element)
        except Exception as e:
            print "login name error:" + str(e)
    
    #点击登录按钮
    def click_login_button(self,driver):
        try:
            login_button = driver.find_element_by_id(self.LOGIN_BUTTON)
            login_button.click()
        except Exception as e:
            print "login button error:" + str(e)
    
    #点击版权所有
    def click_login_copyright(self,driver): 
        pass
        
    #用户名口令认证登录
    def login(self,index,username,pwd):
        #self.set_login_method(self.driver,index)
        #self.set_login_username(username)
        #self.set_login_pwd(self.driver,pwd)
        self.set_login_element(username)
        self.set_login_element(pwd)
        self.click_login_button(self.driver)
        
    #AD域认证登录
    def ad_login(self,driver,loginMethod,username,pwd):
        pass

    #AD域+口令认证登录
    def ad_pwd_login(self,driver,loginMethod,username,pwd):
        pass

    #RADIUS认证登录
    def ad_pwd_login(self,driver,loginMethod,username,pwd):
        pass

    
if __name__ == "__main__":
    #启动页面
    browers = initDriver().open_driver()
    
    loginPage(browers).login(5,"isomper","1")
    
    #关闭页面
    #initDriver().close_driver(browers)