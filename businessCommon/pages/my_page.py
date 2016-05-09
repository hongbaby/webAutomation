from globalUse.Utility import HOSTNAME2
from common.pagebase import PageBase


class MyPage(PageBase):

    ALL_EF_PROGRAM = "All EF Programs"
    LANGUAGE_BUTTON = "English"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/school/mypage/ec"

    def mypage_check(self):
        logo_element = self.get_browser.find_element_by_xpath("//a[@class='ue-underline']/span")

        language_element = self.get_browser.find_element_by_xpath("//a[@class='ue-language-button']/span")

        assert logo_element.text == self.ALL_EF_PROGRAM
        assert language_element.text == self.LANGUAGE_BUTTON
