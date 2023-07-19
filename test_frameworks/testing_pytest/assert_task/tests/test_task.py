import unittest

from _pytest.outcomes import Failed
from selenium import webdriver

from selenium.common import NoAlertPresentException
from test_frameworks.testing_pytest.assert_task.task import test_valid_input
from test_frameworks.testing_pytest.assert_task.task import test_invalid_input

class TestCase(unittest.TestCase):
    def test_valid_valid(self):
        browser = webdriver.Chrome()
        try:
            test_valid_input(browser, 12)
        finally:
            browser.quit()

    def test_valid_invalid(self):
        browser = webdriver.Chrome()
        try:
            self.assertRaises(NoAlertPresentException, test_valid_input, browser, 10001)
        finally:
            browser.quit()

    def test_invalid_valid(self):
        browser = webdriver.Chrome()
        try:
            test_invalid_input(browser, 10001)
        finally:
            browser.quit()

    def test_invalid_invalid(self):
        browser = webdriver.Chrome()
        try:
            self.assertRaises(Failed, test_invalid_input, browser, 123)
        finally:
            browser.quit()
