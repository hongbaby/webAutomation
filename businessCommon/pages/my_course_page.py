# -*- coding: utf-8 -*-
from common.pagebase import PageBase
from globalUse.Utility import HOSTNAME, TIMEOUT_FOR_ELEMENT_WAITING
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class MyCoursePage(PageBase):

    GE_COURSE_NAME = "General English:"
    COURSE_MENU_XPATH = "//span[contains(., 'Course')]"
    COURSE_MY_COURSE_MENU_XPATH = "//a[contains(., 'My course')]"
    COURSE_NAME_XPATH = "//span[@class='ets-chl-current-level-course']"
    CURRENT_LEVEL_NAME_XPATH = "//span[@class='ets-chl-current-level-name']"
    CURRENT_LEVEL_NAME = u"8 – Upper Intermediate"
    UNIT_COUPON_INTERCEPT_PAGE_XPATH = "//div[contains(@class,'efec-unit-pass-container')]"
    UNIT_COUPON_INTERCEPT_PAGE_COUPONS_XPATH = "//div[@id='efec-coupons']"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/school/e12?icid=School.MyCourse.2012"

    @property
    def get_course_web_element(self):

        return self.get_browser.find_element_by_xpath(self.COURSE_MENU_XPATH)

    def go_to_my_course_page(self):
        time.sleep(5)
        self.action_chains_move_to_element(self.get_browser, self.get_course_web_element)
        self.get_browser.find_element_by_xpath(self.COURSE_MY_COURSE_MENU_XPATH).click()
        self.page_is_loaded()

    def wait_for_intercept_page_show_up(self):
        print "Now waiting for intercept page showing:  "
        self.wait_until_element_visible_enabled(self.UNIT_COUPON_INTERCEPT_PAGE_XPATH)
        self.wait_until_element_visible_enabled(self.UNIT_COUPON_INTERCEPT_PAGE_COUPONS_XPATH)

    def wait_until_element_visible_enabled(self, xpath):
        wait = WebDriverWait(self.get_browser, TIMEOUT_FOR_ELEMENT_WAITING)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, xpath)))