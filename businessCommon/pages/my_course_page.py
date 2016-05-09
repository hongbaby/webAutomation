# -*- coding: utf-8 -*-
from common.pagebase import PageBase
from globalUse.Utility import HOSTNAME2, ClassCategory
from selenium.webdriver.support.wait import WebDriverWait

class MyCoursePage(PageBase):

    F2F_COUPON = "efec-f2f-coupons"
    WS_COUPON = "efec-workshop-coupons"
    LC_COUPON = "efec-lifeclub-coupons"
    GE_COURSE_NAME = "General English:"
    COURSE_MENU_XPATH = "//span[contains(., 'Course')]"
    COURSE_MY_COURSE_MENU_XPATH = "//a[contains(., 'My course')]"
    COURSE_NAME_XPATH = "//span[@class='ets-chl-current-level-course']"
    CURRENT_LEVEL_NAME_XPATH = "//span[@class='ets-chl-current-level-name']"
    CURRENT_LEVEL_NAME = u"8 – Upper Intermediate"
    UNIT_COUPON_INTERCEPT_PAGE_XPATH = "//div[contains(@class,'efec-unit-pass-container')]"
    UNIT_COUPON_INTERCEPT_PAGE_COUPONS_XPATH = "//div[@id='efec-coupons']"
    # UNIT_COUPON_INTERCEPT_PAGE_F2F_COUPONS_XPATH = "//div[@id='efec-f2f-coupons']/span[%d]"
    # UNIT_COUPON_INTERCEPT_PAGE_WS_COUPONS_XPATH = "//div[@id='efec-workshop-coupons']"
    # UNIT_COUPON_INTERCEPT_PAGE_LC_COUPONS_XPATH = "//div[@id='efec-lifeclub-coupons']"
    UNIT_COUPON_INTERCEPT_PAGE_CATEGORY_COUPONS_XPATH = "//div[@id='%s']/span[%d]"


    def __init__(self, browser):
        PageBase.__init__(self, browser)
        self.url = "http://" + HOSTNAME2 + "/school/e12?icid=School.MyCourse.2012"

    @property
    def get_course_web_element(self):

        return self.get_browser.find_element_by_xpath(self.COURSE_MENU_XPATH)

    @property
    def get_coupon_name_on_intercept(self, classCoupon=F2F_COUPON):
        return self.get_browser.find_element_by_xpath(self.UNIT_COUPON_INTERCEPT_PAGE_CATEGORY_COUPONS_XPATH % (classCoupon, 2)).text

    def get_coupon_number_on_intercept(self, classCoupon=F2F_COUPON):
        coupon_number = self.get_browser.find_element_by_xpath(self.UNIT_COUPON_INTERCEPT_PAGE_CATEGORY_COUPONS_XPATH % (classCoupon, 1)).text
        print coupon_number
        return coupon_number

    def go_to_my_course_page(self):
        self.action_chains_move_to_element(self.get_browser, self.get_course_web_element)
        self.get_browser.find_element_by_xpath(self.COURSE_MY_COURSE_MENU_XPATH).click()
        self.page_is_loaded()

    def wait_for_intercept_page_show_up(self):
        print "Now waiting for intercept page showing:  "
        self.wait_until_element_visible_enabled(self.UNIT_COUPON_INTERCEPT_PAGE_XPATH)
        self.wait_until_element_visible_enabled(self.UNIT_COUPON_INTERCEPT_PAGE_COUPONS_XPATH)
        self.wait_until_coupon_animation_complete()

    def wait_until_coupon_animation_complete(self, classCategory=ClassCategory.F2F, classCoupon=F2F_COUPON):
        print "Before anomation, the coupon number for %s is: %s" % (classCategory, self.get_coupon_number_on_intercept(classCoupon))
