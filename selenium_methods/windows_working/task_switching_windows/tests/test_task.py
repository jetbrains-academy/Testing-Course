import unittest
from selenium import webdriver
import time
import math

from selenium_methods.windows_working.task_switching_windows.task import redirect_test


def check(reply):
    problem_number = 2306
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
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(10)
            redirect_test(browser)
            reply = browser.switch_to.alert.text
            self.assertTrue(check(reply))
        finally:
            browser.quit()
