import unittest

from globalUse.page_base import PageBase
from businessCommon.pages.my_course_page import MyCoursePage
from common.common_function import action_chains_move_to_element, wait_for_element_visible, get_element1


class MyCoursePageCheck(PageBase):

    def test_current_course_name_check(self):

        course_element = self.driver.find_element_by_xpath(MyCoursePage.COURSE_MENU_XPATH)
        action_chains_move_to_element(self.driver, course_element, MyCoursePage.COURSE_MY_COURSE_MENU_XPATH)

        course_name_element = get_element1(self.driver, MyCoursePage.COURSE_NAME_XPATH)
        wait_for_element_visible(self.driver, course_name_element)

        assert course_name_element.text == MyCoursePage.GE_COURSE_NAME

    def test_current_level_check(self):

        course_element = self.driver.find_element_by_xpath(MyCoursePage.COURSE_MENU_XPATH)
        action_chains_move_to_element(self.driver, course_element, MyCoursePage.COURSE_MY_COURSE_MENU_XPATH)

        current_level_name_element = get_element1(self.driver, MyCoursePage.CURRENT_LEVEL_NAME_XPATH)
        wait_for_element_visible(self.driver, current_level_name_element)

        assert current_level_name_element.text == MyCoursePage.CURRENT_LEVEL_NAME


if __name__ == '__main__':
    unittest.main()