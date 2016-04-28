import unittest
from selenium import webdriver
from businessCommon.business_common_function import log_in
from globalUse.Utility import IMPLICITLY_WAIT_TIME, ROOT_URL


class PageBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT_TIME)
        self.driver.get(ROOT_URL)
        log_in(self.driver)

    def tearDown(self):
        self.driver.quit()