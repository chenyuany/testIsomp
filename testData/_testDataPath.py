#coding=utf-8
#设定excel数据文件名字，统一调用
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _excelRead import excelRead

#通用数据excel文件
COMMON_SUITE_TEST_DATA_URL = r"/testIsomp/testData/common_suite_test_data.xlsx"
#登陆excel数据文件
LOGIN_TEST_DATA_URL = r"/testIsomp/testData/login_test_data.xlsx"

#用户excel数据位置
USER_TEST_DATA_URL = r"/testIsomp/testData/user_test_data.xlsx"

#角色定义数据文件
ROLE_TEST_DATA_URL = r"/testIsomp/testData/role_test_data.xlsx"

#组织定义数据文件
DEPARTMENT_TEST_DATA_URL = r"/testIsomp/testData/department_test_data.xlsx"

#认证方式数据文件
AUTH_METHOD_TEST_DATA_URL = r"/testIsomp/testData/auth_method_test_data.xlsx"

#授权数据文件
AUTHORIZATION_TEST_DATA_URL = r"/testIsomp/testData/authorization_test_data.xlsx"

#linux资源数据文件
LINUX_RESOURCE_TEST_DATA_URL = r"/testIsomp/testData/linux_resource_test_data.xlsx"

#网络设备资源数据位置
NETWORK_RESOURCE_TEST_DATA_URL = r"/testIsomp/testData/network_resource_test_data.xlsx"

#资源组数据文件
REGROUP_TEST_DATA_URL = r"/testIsomp/testData/regroup_test_data.xlsx"

#用户组数据文件
USERGROUP_TEST_DATA_URL = r"/testIsomp/testData/usergroup_test_data.xlsx"

class dataFileName(object):
    #获取通用excel中的数据
    def get_common_suite_test_data_url(self):
        return COMMON_SUITE_TEST_DATA_URL
    
    #获取用户登录excel中的数据
    def get_login_test_data_url(self):
        return LOGIN_TEST_DATA_URL
    
    #获取认证方式excel中的数据
    def get_auth_method_test_data_url(self):
       return AUTH_METHOD_TEST_DATA_URL 
    
    #获取用户excel中的数据
    def get_person_test_data_url(self):
        return USER_TEST_DATA_URL
    
    #获取授权excel中的数据
    def get_authorization_test_data_url(self):
        return AUTHORIZATION_TEST_DATA_URL

    u"""获取角色定义数据文件的数据"""
    def get_role_test_data_url(self):
        return ROLE_TEST_DATA_URL

    u"""获取组织定义部门文件的数据"""
    def get_depart_test_data_url(self):
        return DEPARTMENT_TEST_DATA_URL

    u"""获取linux资源文件的数据"""
    def get_linux_resource_test_data_url(self):
        return LINUX_RESOURCE_TEST_DATA_URL

    u"""获取资源组文件的数据"""
    def get_regroup_test_data_url(self):
        return REGROUP_TEST_DATA_URL

    u"""获取用户组文件的数据"""
    def get_usergroup_test_data_url(self):
        return USERGROUP_TEST_DATA_URL

    u"""获取网络设备资源文件的数据"""
    def get_network_resource_test_data_url(self):
        return NETWORK_RESOURCE_TEST_DATA_URL

    #从sheet名称获取登陆数据
    def get_data(self,dataPath,sheetName):
        #获取excel数据
        data = excelRead().get_excel_data(dataPath,sheetName)
        
        return data
    
#dataFile = dataFileName()
#login_data = dataFileName().get_data(dataFileName().get_auth_method_test_data_url(),'add_auth_method')
#for dataRow in range(len(login_data)):
#    data = login_data[dataRow]
#    print data
    