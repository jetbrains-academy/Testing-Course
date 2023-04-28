import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException

from introduction.finding_elements_selenium.task10.task import finding_unique_selectors


class TestCase(unittest.TestCase):
    def test_add(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        try:
            self.assertRaises(NoSuchElementException, finding_unique_selectors, browser)
        finally:
            browser.quit()
