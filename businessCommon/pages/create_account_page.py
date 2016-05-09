from common.pagebase import PageBase
from globalUse.Utility import HOSTNAME2
from globalUse.create_account_info import account_info, Partners, ProductType, LevelInfoCool
from selenium import webdriver


class CreateAccountPage(PageBase):

    ACTIVATE_XPATH = "/html/body/a"
    BODY_XPATH_IN_CREATE_ACCOUNT = "/html/body"
    SUBMIT_BUTTON_XPATH = "//input[@type='submit']"
    BODY_XPATH_IN_SUBMIT_ACCOUNT = "/html/body"
    LEVEL_RADIO_XPATH = "/html/body/form/ul/li[2]/input"

    ACCOUNT_INFO_XPATH_FORMAT = "//input[@name='%s']"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/services/oboe2/salesforce/test/CreateMemberForE14HZ"

    def get_username(self):
        all_info = self.get_browser.find_element_by_xpath(self.BODY_XPATH_IN_CREATE_ACCOUNT).text
        user_info = all_info.split(',')[2].strip()
        username = user_info.split(":")[1].strip()

        return username

    def submit_product_info(self, startLevel, partner, product):
        self.choose_start_level(startLevel)
        self.fill_basic_product_info(partner, product)
        self.get_browser.find_element_by_xpath(self.SUBMIT_BUTTON_XPATH).submit()
        self.page_is_loaded()
        result_info = self.get_browser.find_element_by_xpath(self.BODY_XPATH_IN_SUBMIT_ACCOUNT).text

        return result_info

    def choose_start_level(self, startLevel):
        radios = self.get_browser.find_elements_by_xpath(self.LEVEL_RADIO_XPATH)
        for radio in radios:
            if str(radio.get_attribute("value")) == startLevel:
                radio.click()
                break

    def fill_basic_product_info(self, partner, product):
        for info in account_info:
            tags = info["tags"]
            if tags["partner"] == partner and tags["Product Type"] == product:
                break

        for key, value in info.items():
            if key != "tags":
                element = self.get_browser.find_element_by_xpath(self.ACCOUNT_INFO_XPATH_FORMAT % key)
                element.clear()
                element.send_keys(value)

    @staticmethod
    def submit_result_check(result_string):
        result = False
        if result_string.startswith("success"):
            result = True
            return result
        else:
            print "create account failed. %s" % result_string.split(",")[3].strip()
            return result

    def activate_account(self, startLevel=LevelInfoCool.LEVEL_1, partner=Partners.COOL, product=ProductType.School):
        self.get_url()
        username = self.get_username()
        self.get_browser.find_element_by_xpath(self.ACTIVATE_XPATH).click()
        self.switch_to_other_tab(self.get_browser.current_window_handle)
        result_info = self.submit_product_info(startLevel, partner, product)

        if self.submit_result_check(result_info):
            print "create account successfully! The username is: %s" % username
            return username

if __name__ == "__main__":
    driver = webdriver.Chrome()
    CreateAccountPage(driver).activate_account()