import math
import pytest
from selenium.webdriver.common.by import By
from selenium.common import NoAlertPresentException

link = "https://suninjuly.github.io/divide.html"


def test_valid_input(browser, input):
    browser.get(link)
    x = browser.find_element(By.ID, "input-value")
    x.send_keys(input)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    alert = browser.switch_to.alert
    expected = math.log((abs(12*math.sin(input))))
    actual = alert.text
    assert alert.text == str(math.log((abs(12*math.sin(input))))), f"expected {expected}, got {actual}"


def test_invalid_input(browser, input):
    browser.get(link)
    with pytest.raises (NoAlertPresentException):
        x = browser.find_element(By.ID, "input-value")
        x.send_keys(input)
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.CSS_SELECTOR, ".btn").click()
        alert = browser.switch_to.alert
        expected = math.log((abs(12*math.sin(input))))
        actual = alert.text
        assert alert.text == str(math.log((abs(12*math.sin(input))))), f"expected {expected}, got {actual}"

