from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage
from businessCommon.pages.my_course_page import MyCoursePage
from businessCommon.pages.create_account_page import CreateAccountPage


class MyCoursePageOpened(FrontEndTestCase):

    def runTest(self):
        username = CreateAccountPage(self.driver).activate_account()
        EtownLoginPage(self.driver).log_in(username)

        MyCoursePage(self.driver).go_to_my_course_page()

        assert self.browser.current_url == MyCoursePage(self.driver).url

if __name__ == '__main__':
    MyCoursePageOpened().runTest()