from selenium import webdriver
from globalUse.Utility import IMPLICITLY_WAIT_TIME
from main import kill_process


class FrontEndTestCase(object):

    def create_browser_driver(self):
        # # chromedriver = "/usr/local/bin/chromedriver"
        # # os.environ["webdriver.chrome.driver"] = chromedriver
        # self.driver = webdriver.Chrome("/usr/bin/chromedriver")
        kill_process("taskkill /F /IM chromedriver.exe")
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT_TIME)

        return self.driver

    def runTest(self):

        raise NotImplementedError("sub class %s must implement this runTest(self) method: " % self)

    def quit_browser_driver(self):
        self.driver.quit()
