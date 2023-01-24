from selenium.webdriver.common.by import By


def long_form_script(browser):
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        element.send_keys("my answer")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
