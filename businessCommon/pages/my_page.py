from globalUse.Utility import HOSTNAME
from common.pagebase import PageBase


class MyPage(PageBase):

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/school/mypage/ec"

    def mypage_check(self):
        logo_element = self.get_browser.find_element_by_xpath("//a[@class='ue-underline']/span")

        language_element = self.get_browser.find_element_by_xpath("//a[@class='ue-language-button']/span")

        print logo_element.text
        assert logo_element.text == "All EF Programs"
        print language_element.text
        assert language_element.text == "English"
