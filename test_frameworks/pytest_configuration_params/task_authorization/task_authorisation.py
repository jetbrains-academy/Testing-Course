from selenium.webdriver.common.by import By

lesson_link = "https://stepik.org/lesson/236895/step/1"


def test_authorisation(browser):
    browser.get(lesson_link)
    browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login").click()
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("email")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("password")
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()
