from common.front_end_test_case import FrontEndTestCase
from businessCommon.pages.login_page import EtownLoginPage, MyPage


class MyPageOpenedCheck(FrontEndTestCase):

    def runTest(self):
        self.browser = self.create_browser_driver()

        EtownLoginPage(self.browser).log_in()
        MyPage(self.browser).mypage_check()

        self.browser.quit()

if __name__ == '__main__':
    MyPageOpenedCheck().runTest()