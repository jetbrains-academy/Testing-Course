import time

from selenium import webdriver

# importing class By, which allows to search elements
from selenium.webdriver.common.by import By


def first_script():
    # initializing new browser instance. You should see new window at this point
    driver = webdriver.Chrome()
    time.sleep(5)

    # get method allows to open URL
    driver.get("https://suninjuly.github.io/text_input_task.html")
    time.sleep(5)

    # find_element method allows to find element on page. We discuss different searching methods further in the course
    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

    # Writing text in text field
    textarea.send_keys("get()")
    time.sleep(5)

    # find submit button
    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

    # clicking submit button
    submit_button.click()
    time.sleep(5)

    # closing browser
    driver.quit()
