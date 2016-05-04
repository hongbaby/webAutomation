from common.pagebase import PageBase
from globalUse.Utility import HOSTNAME
from selenium import webdriver

class CreateAccountPage(PageBase):

    ACTIVATE_XPATH = "/html/body/a"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/services/oboe2/salesforce/test/CreateMemberForE14HZ"

    def create_account(self):
        self.get_url()
        username = self.get_username()
        self.get_browser.find_element_by_xpath(self.ACTIVATE_XPATH).click()

    def get_username(self):
        all_info = self.get_browser.find_element_by_xpath("/html/body").text
        user_info = all_info.split(',')[2].strip()
        username = user_info.split(":")[1].strip()

        return username

    def submit_product_info(self):
        pass