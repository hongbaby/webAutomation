from common.pagebase import PageBase
from businessCommon.pages.my_page import MyPage
from businessCommon.pages.create_account_page import CreateAccountPage
from globalUse.Utility import LOGIN_URL, USERNAME, PASSWORD


class EtownLoginPage(PageBase):

    USER_NAME_ID = "username"
    PASS_WORD_ID = "password"
    SIGN_IN_CLASS = "etc-login-btn"
    START_LEARNING_BUTTON_XPATH = "//button[contains(., 'START LEARNING')]"
    CLASS_REMINDER_CLOSE_XPATH = "//a[@class='ets-ecc-lightbox-classesreminder-close']"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = LOGIN_URL

    def log_in(self, username=USERNAME, password=PASSWORD):
        self.get_url()
        self.get_browser.find_element_by_id(self.USER_NAME_ID).send_keys(username)
        self.get_browser.find_element_by_id(self.PASS_WORD_ID).send_keys(password)
        self.get_browser.find_element_by_class_name(self.SIGN_IN_CLASS).click()
        self.start_learning()
        self.close_class_reminder()

        assert self.get_browser.current_url == MyPage(self.get_browser).url

    def start_learning(self):
        self.get_browser.find_element_by_xpath(self.START_LEARNING_BUTTON_XPATH).click()

    def close_class_reminder(self):
        self.get_browser.find_element_by_xpath(self.CLASS_REMINDER_CLOSE_XPATH).click()
