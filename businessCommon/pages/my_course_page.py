# -*- coding: utf-8 -*-
from common.pagebase import PageBase
from globalUse.Utility import HOSTNAME


class MyCoursePage(PageBase):

    GE_COURSE_NAME = "General English:"
    COURSE_MENU_XPATH = "//span[contains(., 'Course')]"
    COURSE_MY_COURSE_MENU_XPATH = "//a[contains(., 'My course')]"
    COURSE_NAME_XPATH = "//span[@class='ets-chl-current-level-course']"
    CURRENT_LEVEL_NAME_XPATH = "//span[@class='ets-chl-current-level-name']"
    CURRENT_LEVEL_NAME = u"8 – Upper Intermediate"

    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME + "/school/e12?icid=School.MyCourse.2012"

    @property
    def get_course_web_element(self):

        return self.get_browser.find_element_by_xpath(self.COURSE_MENU_XPATH)

    def go_to_my_course_page(self):
        self.action_chains_move_to_element(self.get_browser, self.get_course_web_element)
        self.get_browser.find_element_by_xpath(self.COURSE_MY_COURSE_MENU_XPATH).click()
        self.page_is_loaded()