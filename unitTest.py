from selenium import webdriver
import unittest
from globalUse.Utility import USERNAME, PASSWORD, LOGIN_URL


class UnitTestClass(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    # def test_login(self, username=USERNAME, password=PASSWORD):
    #     self.driver.get(LOGIN_URL)
    #     self.driver.find_element_by_id("username").send_keys(username)
    #     self.driver.find_element_by_id("password").send_keys(password)
    #     self.driver.find_element_by_class_name("etc-login-btn").click()

    def test_activate_tool(self):
        self.driver.get("http://qa.englishtown.com/services/oboe2/salesforce/test/CreateMemberForE14HZ")
        usr_info = self.driver.find_element_by_xpath("/html/body").text
        user_info = usr_info.split(',')[2].strip()
        username = user_info.split(":")[1]

        print username.strip()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
