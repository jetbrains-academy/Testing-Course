from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/huge_form.html"


def long_form_script(browser):
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text']")
    for element in elements:
        element.send_keys("my answer")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
