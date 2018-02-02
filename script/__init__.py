
# 新建短信
from selenium.webdriver.common.by import By

xj = (By.ID, "com.android.mms:id/action_compose_new")
# 接收者
js = (By.ID, "com.android.mms:id/recipients_editor")
# 进入信息
xx = (By.ID, "com.android.mms:id/embedded_text_editor")
# 发送
fs = (By.ID, "com.android.mms:id/send_button_sms")