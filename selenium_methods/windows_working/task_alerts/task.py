import math
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"


def alert_accept(browser):
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)
    random_value = browser.find_element(By.ID, "input_value").text
    answer = (math.log(abs((12 * math.sin(float(random_value))))))
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(str(answer))
    browser.find_element(By.TAG_NAME, "button").click()
