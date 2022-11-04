# todo: replace this with an actual task
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"


def first_script(browser):
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "value1")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "value2")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "value3")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "value4")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "value5")
    button.click()

