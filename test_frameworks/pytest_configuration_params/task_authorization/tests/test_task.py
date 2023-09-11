import unittest
from selenium import webdriver

from test_frameworks.pytest_configuration_params.task_authorization.task_authorisation import test_authorisation


class TestCase(unittest.TestCase):
    def test_script(self):
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(10)
            test_authorisation(browser)
        finally:
            browser.quit()
