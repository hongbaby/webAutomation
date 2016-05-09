from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage
from businessCommon.pages.my_course_page import MyCoursePage
from businessCommon.pages.create_account_page import CreateAccountPage


class MyCourseInterceptPageCheck(FrontEndTestCase):

    def runTest(self):
        username = CreateAccountPage(self.driver).activate_account()
        EtownLoginPage(self.driver).log_in(username)

        MyCoursePage(self.driver).go_to_my_course_page()

        MyCoursePage(self.driver).wait_for_intercept_page_show_up()

if __name__ == '__main__':
    MyCourseInterceptPageCheck().runTest()