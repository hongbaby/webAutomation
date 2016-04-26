from globalUse.Utility import USERNAME, PASSWORD


def log_in(driver, username=USERNAME, password=PASSWORD):

    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_class_name("etc-login-btn").click()

    assert driver.current_url == "http://ec.ef.com.cn/school/mypage/ec"
