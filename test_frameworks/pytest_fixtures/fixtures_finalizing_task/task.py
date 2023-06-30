import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

filename = "answer.txt"
link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # this code evaluates after test is finished
    print("\nquit browser..")
    browser.quit()


@pytest.fixture
def answer_file():
    if os.path.exists(filename):
        os.remove(filename)
    f = open(filename, "x")
    yield f
    f.close()
    os.remove(filename)


def test_math(browser, answer_file):
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox").click()
    robot_radio = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    answer_file.write(alert.text.split(": ", 1)[1])
