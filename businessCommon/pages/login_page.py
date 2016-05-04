from common.pagebase import PageBase
from businessCommon.pages.my_page import MyPage
from globalUse.Utility import LOGIN_URL, USERNAME, PASSWORD


class EtownLoginPage(PageBase):

    USER_NAME_ID = "username"
    PASS_WORD_ID = "password"
    SIGN_IN_CLASS = "etc-login-btn"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = LOGIN_URL

    def log_in(self):
        self.get_url()
        self.get_browser.find_element_by_id(self.USER_NAME_ID).send_keys(USERNAME)
        self.get_browser.find_element_by_id(self.PASS_WORD_ID).send_keys(PASSWORD)
        self.get_browser.find_element_by_class_name(self.SIGN_IN_CLASS).click()

        assert self.get_browser.current_url == MyPage(self.get_browser).url
