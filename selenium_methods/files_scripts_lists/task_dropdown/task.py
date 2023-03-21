from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/selects1.html"


def select1(browser):
    browser.get(link)
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    answer = str(int(num1) + int(num2))
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(answer)
    browser.find_element(By.TAG_NAME, "button").click()
