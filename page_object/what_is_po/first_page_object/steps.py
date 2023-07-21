from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math

from selenium.webdriver.support.wait import WebDriverWait


def solve_quiz(browser):
    random_value = browser.find_element(By.ID, "input_value").text
    answer = (math.log(abs((12 * math.sin(float(random_value))))))
    text_field = browser.find_element(By.ID, "answer")
    text_field.send_keys(str(answer))
    browser.find_element(By.ID, "solve").click()


def wait_for_price(browser, price):
    price_text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )


def should_be_math_text(browser):
    assert browser.find_element(By.ID, "simple_text").text == "Math is real magic!"


def book(browser):
    button = browser.find_element(By.ID, "book")
    button.click()
