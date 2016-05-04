from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage
from businessCommon.pages.my_course_page import MyCoursePage


class MyCoursePageCurrentLevelCheck(FrontEndTestCase):

    def runTest(self):
        self.browser = self.create_browser_driver()

        EtownLoginPage(self.browser).log_in()
        MyCoursePage(self.browser).go_to_my_course_page()

        self.browser.quit_browser_driver()

if __name__ == '__main__':
    MyCoursePageCurrentLevelCheck().runTest()