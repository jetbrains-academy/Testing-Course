from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"


def safe_script():
    browser = webdriver.Chrome()
    try:
        browser.get(link)
        button = browser.find_element(By.ID, "submit_button")
        button.click()
    finally:
        # closing browser no matter what happened
        browser.quit()


def not_safe_script():
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

    # closing the browser after all operations
    browser.quit()
