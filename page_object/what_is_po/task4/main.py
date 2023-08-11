link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page_new(browser):
    browser.get(link)
    go_to_login_page(browser)

