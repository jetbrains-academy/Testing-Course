import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver

from introduction.finding_elements.find_child_element.task import child_selector


class TestCase(unittest.TestCase):
    def test_add(self):
        self.assertFalse("body" in child_selector, "Should be no 'body' in selector")
        self.assertFalse("[" in child_selector or "]" in child_selector, "Should be no '[]' in selector'")
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(4)
            browser.get("http://suninjuly.github.io/cats.html")
            element = browser.find_element(By.CSS_SELECTOR, child_selector)
            print(element.get_attribute("src"))
            self.assertTrue(element.get_attribute("src") == "http://suninjuly.github.io/images/serious_cat.jpg")
        finally:
            browser.quit()
