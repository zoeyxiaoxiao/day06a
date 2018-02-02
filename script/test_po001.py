import pytest
from selenium.webdriver.common.by import By
import sys,os
sys.path.append(os.getcwd())
from appium import webdriver
from script.Search import Search_Page

class Test_sedrch:
    def setup_class(self):
        desired_caps = {}
        desired_caps["platformName"] = "Android"
        desired_caps["platformVersion"] = "5.1"
        # 设备号
        desired_caps["deviceName"] = "192.168.39.101:5555"
        # 启动名
        desired_caps['appPackage'] = 'com.android.mms'
        # 包名
        desired_caps['appActivity'] = 'ui.ConversationList'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.search_obj = Search_Page(self.driver)

    def teardown_class(self):
        self.driver.quit()
    def test_aaa(self):
        self.search_obj.search_text1()

    def test_bbb(self):
        self.search_obj.search_text2('18518636266')

    @pytest.mark.parametrize("text",[1,2,3])
    def test_ccc(self,text):
        self.search_obj.search_text3(text)
    #
    def test_ddd(self):
        self.search_obj.search_text4()
