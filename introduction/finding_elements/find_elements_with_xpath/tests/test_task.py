import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver

from introduction.finding_elements.find_elements_with_xpath.task import xPath


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertFalse("body" in xPath, "Should be no 'body' in selector")
        self.assertFalse("html" in xPath , "Should be no 'html' in selector'")
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(4)
            browser.get("http://suninjuly.github.io/xpath_examples")
            element = browser.find_element(By.XPATH, xPath)
            self.assertTrue(element.text == "Gold")
        finally:
            browser.quit()
