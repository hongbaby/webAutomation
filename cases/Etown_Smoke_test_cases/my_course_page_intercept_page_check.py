from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage
from businessCommon.pages.my_course_page import MyCoursePage
from businessCommon.pages.create_account_page import CreateAccountPage


class MyCourseInterceptPageCheck(FrontEndTestCase):

    def runTest(self):
        self.browser = self.create_browser_driver()

        username = CreateAccountPage(self.browser).activate_account()
        EtownLoginPage(self.browser).log_in(username)

        MyCoursePage(self.browser).go_to_my_course_page()

        MyCoursePage(self.browser).wait_for_intercept_page_show_up()

        self.browser.quit()

if __name__ == '__main__':
    MyCourseInterceptPageCheck().runTest()