from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage, MyPage
from businessCommon.pages.create_account_page import CreateAccountPage


class MyPageOpenedCheck(FrontEndTestCase):

    def runTest(self):
        username = CreateAccountPage(self.driver).activate_account()
        EtownLoginPage(self.driver).log_in(username)
        MyPage(self.driver).mypage_check()

if __name__ == '__main__':
    MyPageOpenedCheck().runTest()