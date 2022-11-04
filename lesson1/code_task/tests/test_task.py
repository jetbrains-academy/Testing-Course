import unittest
import time
import math
from selenium import webdriver

from lesson1.code_task.task import first_script

def check_reply(reply):
    problem_number = 3
    minutes_to_delay = 5

    ts_now = int(time.time())
    ts_past = ts_now - 60*minutes_to_delay

    hashcode_now = math.log(ts_now*problem_number)
    hashcode_past = math.log(ts_past*problem_number)
    try:
        replys = float(reply)
        if  (replys < hashcode_now and replys > hashcode_past):
            return True
        else:
            return False

    except ValueError:
        return 0, "Неверный формат строки, должно быть число"


class TestCase(unittest.TestCase):
    def test_script(self):
        try:
            print("test script1")
            browser = webdriver.Chrome()
            first_script(browser)
            reply = browser.switch_to.alert.text
            self.assertTrue(check_reply(reply))
        finally:
            browser.quit()

if __name__ == '__main__':
    unittest.main()
