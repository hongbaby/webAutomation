from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from globalUse.Utility import PAGE_LOADING_TIME_OUT


class PageBase(object):

    def __init__(self, browser):
        self._browser = browser
        self.url = ''

    @property
    def get_browser(self):
        return self._browser

    def get_url(self):
        self.get_browser.get(self.url)

    def action_chains_move_to_element(self, browser, web_element):
        ActionChains(browser).move_to_element(web_element).perform()

    def page_is_loaded(self):

        self.get_browser.set_page_load_timeout(PAGE_LOADING_TIME_OUT)

    def switch_to_other_tab(self, current_handle):

        all_handles = self.get_browser.window_handles
        for handle in all_handles:
            if handle != current_handle:
                self.get_browser.switch_to_window(handle)
                return current_handle