from common.pagebase import PageBase
from globalUse.Utility import HOSTNAME
from globalUse.create_account_info import account_info, Partners, ProductType, LevelInfoCool
from selenium import webdriver


class CreateAccountPage(PageBase):

    ACTIVATE_XPATH = "/html/body/a"
    BODY_XPATH_IN_CREATE_ACCOUNT = "/html/body"
    SUBMIT_BUTTON_XPATH = "//input[@type='submit']"
    BODY_XPATH_IN_SUBMIT_ACCOUNT = "/html/body"
    LEVEL_RADIO_XPATH = "/html/body/form/ul/li[2]/input"
    MAIN_REDEMPTION_CODE = "//input[@name='mainRedemptionCode']"
    FREE_REDEMPTION_CODE = "//input[@name='freeRedemptionCode']"
    DIVISION_CODE_XPATH = "//input[@name='divisionCode']"
    PRODUCT_ID_XPATH = "//input[@name='productId']"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/services/oboe2/salesforce/test/CreateMemberForE14HZ?v=2"

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
            if info["partner"] == partner and info["Product Type"] == product:
                break

        main_redemption_code_element = self.get_browser.find_element_by_xpath(self.MAIN_REDEMPTION_CODE)
        main_redemption_code_element.clear()
        main_redemption_code_element.send_keys(info["MainRedemptionCode"])

        free_redemption_code_element = self.get_browser.find_element_by_xpath(self.FREE_REDEMPTION_CODE)
        free_redemption_code_element.clear()
        free_redemption_code_element.send_keys(info["FreeRedemptionCode"])

        division_code_element = self.get_browser.find_element_by_xpath(self.DIVISION_CODE_XPATH)
        division_code_element.clear()
        division_code_element.send_keys(info["DivisionCode"])

        product_id_element = self.get_browser.find_element_by_xpath(self.PRODUCT_ID_XPATH)
        product_id_element.clear()
        product_id_element.send_keys(info["Product ID"])

    @staticmethod
    def submit_result_check(result_string):
        result = False
        if result_string.startswith("success"):
            result = True
            return result
        else:
            print "create account failed. %s" % result_string.split(",")[3].strip()
            return result

    def activate_account(self, startLevel=LevelInfoCool.LEVEL_1, partner=Partners.MINI, product=ProductType.Home):
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