from selenium.webdriver.common.by import By

lesson_link = "https://stepik.org/lesson/236895/step/1"

def test_authorisation(browser):
    # Логинимся
    email = browser.find_element(By.ID, "id_login_email")
    email.send_keys("chesika968@mail.ru")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("cbcmrb0m")
    button = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']")
    button.click()