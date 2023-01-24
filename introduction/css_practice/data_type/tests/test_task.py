import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from introduction.css_practice.data_type.task import data_selector


class TestCase(unittest.TestCase):
    def test_script(self):
        self.assertFalse("body" in data_selector, "Selector shouldn't contain 'body'")
        self.assertTrue("data-type" in data_selector, "Selector should use 'data-type attribute'")
        try:
            browser = webdriver.Chrome()
            browser.get("http://localhost:63342/UI test automation with Selenium and Python/introduction/css_practice/data_type/index.html?_ijt=502p5tptbli1d6o9f5dm01h1du")
            element = browser.find_element(By.CSS_SELECTOR, data_selector)
            elements = browser.find_elements(By.CSS_SELECTOR, data_selector)
            self.assertTrue(len(elements) == 1, "Should be only one element found with the selector")
            self.assertTrue(element.text == "Nice cat", "'Nice cat' description should be found with the selector")
        finally:
            browser.quit()

if __name__ == '__main__':
    unittest.main()
