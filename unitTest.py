from selenium import webdriver
import unittest
from globalUse.Utility import ROOT_URL


class UnitTestClass(unittest.TestCase):

    driver = webdriver.Firefox()

    def setUp(self):
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    def test_login(self, username='khongc15', password='1'):
        self.driver.get(ROOT_URL)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_class_name("etc-login-btn").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()