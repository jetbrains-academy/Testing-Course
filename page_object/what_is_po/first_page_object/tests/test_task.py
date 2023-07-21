import unittest
from selenium import webdriver
import time
import math

from page_object.what_is_po.first_page_object.task import *
from page_object.what_is_po.first_page_object.steps import *


def check(reply):
    problem_number = 2408
    minutes_to_delay= 5

    ts_now = int(time.time())
    ts_past = ts_now - 60*minutes_to_delay

    hashcode_now = math.log(ts_now*problem_number)
    hashcode_past = math.log(ts_past*problem_number)
    try:
        replys = float(reply)
        if  (replys < hashcode_now and replys > hashcode_past):
            return True
        elif replys <= hashcode_past:
            return 0, "Срок действия кода истек, попробуйте еще раз"
        else:
            return 0, "Неверный код"

    except ValueError:
        return 0, "Неверный формат строки, должно быть число"


class TestCase(unittest.TestCase):
    def test_script(self):
        browser = webdriver.Chrome()
        try:
            browser.implicitly_wait(10)
            wait_test(browser)
        finally:
            browser.quit()

    def test_wait(self):
        browser = webdriver.Chrome()
        try:
            browser.implicitly_wait(10)
            browser.get(link)
            wait_for_price(browser, "100$")
            book(browser)
            should_be_math_text(browser)
            solve_quiz(browser)
            reply = float(browser.switch_to.alert.text.split(": ")[1])
            self.assertTrue(check(reply))
        finally:
            browser.quit()

    def test_wait_negative(self):
        browser = webdriver.Chrome()
        try:
            browser.implicitly_wait(10)
            browser.get("https://suninjuly.github.io/explicit_wait3.html")
            wait_for_price(browser, "100$")
            book(browser)
            self.assertRaises(AssertionError, should_be_math_text, browser)
        finally:
            browser.quit()