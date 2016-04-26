# -*- coding: utf-8 -*-
import unittest
from globalUse.page_base import PageBase


class MyPageCheck(PageBase):

    def test_footer_check(self):
        logo_element = self.driver.find_element_by_xpath("//a[@class='ue-underline']/span")
        print logo_element.text
        assert logo_element.text == "All EF Programs"

    def test_footer_language_check(self):
        language_element = self.driver.find_element_by_xpath("//a[@class='ue-language-button']/span")
        print language_element.text
        assert language_element.text == "English"

if __name__ == '__main__':
    unittest.main()
