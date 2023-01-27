import os
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"


def file_input(browser):
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("IvanOff")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("ivan666@mail.ru")
    input4 = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
