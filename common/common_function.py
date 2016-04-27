from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from globalUse.Utility import TIMEOUT_FOR_ELEMENT_WAITING

def action_chains_move_to_element(driver, web_element, web_locator):
    ActionChains(driver).move_to_element(web_element).perform()
    driver.find_element_by_xpath(web_locator).click()


def wait_for_element_visible(driver, web_Element):

    WebDriverWait(driver, 60).until(expected_conditions.visibility_of(web_Element))


def get_element(driver, xpath):

    def method_in_until(driver):

        driver.find_element_by_xpath(xpath)

    element = WebDriverWait(driver, 60).until(method_in_until)

    return element


def get_element1(driver, xpath, timeout=TIMEOUT_FOR_ELEMENT_WAITING):
    wait = WebDriverWait(driver, timeout)
    # element_expression = lambda x: x.find_element_by_xpath(xpath)

    def test_condition(driver):
        elements = driver.find_elements_by_xpath(xpath)
        if len(elements) > 0:
            return elements[0]
        else:
            return False

    # element_expression = lambda x: len(x.find_elements_by_xpath(xpath)) > 0

    try:
        print "Looking for element %s within %s seconds" % (xpath, timeout)
        element = wait.until(test_condition)
        print element

    except TimeoutException:
        error_message = "Can not find element with xpath '%s'" % xpath
        raise TimeoutException, error_message

    return element