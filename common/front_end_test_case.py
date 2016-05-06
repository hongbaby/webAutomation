from selenium import webdriver
from globalUse.Utility import IMPLICITLY_WAIT_TIME


class FrontEndTestCase(object):

    def create_browser_driver(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT_TIME)

        return self.driver

    def runTest(self):

        raise NotImplementedError("sub class %s must implement this runTest(self) method: " % self)

    def quit_browser_driver(self):
        self.driver.quit()
