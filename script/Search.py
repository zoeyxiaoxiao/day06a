from selenium.webdriver.common.by import By
from Base.Base import Base
import script
class Search_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        # # 新建短信
        # self.xj = (By.ID,"com.android.mms:id/action_compose_new")
        # # 接收者
        # self.js = (By.ID,"com.android.mms:id/recipients_editor")
        # # 进入信息
        # self.xx = (By.ID,"com.android.mms:id/embedded_text_editor")
        # #发送
        # self.fs = (By.ID,"com.android.mms:id/send_button_sms")
        # 实例化
        # self.base_obj = Base(driver)

    def search_text1(self):
        # 新建短信
        self.click_element(script.xj)

    def search_text2(self,text):
        # 输入接收者
        self.input_element(script.js,text)

    def search_text3(self,text):
        # 进入信息
        self.input_element(script.xx,text)

    def search_text4(self):
        self.click_element(script.fs)
