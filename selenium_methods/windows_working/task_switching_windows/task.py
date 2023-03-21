import math
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"


def redirect_test(browser):
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    random_value = browser.find_element(By.ID, "input_value").text
    answer = (math.log(abs((12 * math.sin(float(random_value))))))
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(str(answer))
    browser.find_element(By.TAG_NAME, "button").click()
