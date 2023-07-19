import unittest

from selenium import webdriver
from introduction.finding_elements_selenium.unique_selectors.task import finding_unique_selectors


class TestCase(unittest.TestCase):
    def test_add(self):
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        try:
            finding_unique_selectors(browser)
        finally:
            browser.quit()
