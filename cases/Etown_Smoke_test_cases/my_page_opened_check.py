from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage, MyPage
from businessCommon.pages.create_account_page import CreateAccountPage


class MyPageOpenedCheck(FrontEndTestCase):

    def runTest(self):
        self.browser = self.create_browser_driver()

        username = CreateAccountPage(self.browser).activate_account()
        EtownLoginPage(self.browser).log_in(username)
        MyPage(self.browser).mypage_check()

        self.browser.quit()

if __name__ == '__main__':
    MyPageOpenedCheck().runTest()