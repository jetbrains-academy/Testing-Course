import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def get_attribute(browser):
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    robot_radio = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
