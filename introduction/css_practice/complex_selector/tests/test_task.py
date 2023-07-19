import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from introduction.css_practice.complex_selector.task import complex_selector


class TestCase(unittest.TestCase):
    def test_script(self):
        self.assertFalse("body" in complex_selector, "Selector shouldn't contain 'body'")
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.get("https://suninjuly.github.io/css-tasks/complex")
            element = browser.find_element(By.CSS_SELECTOR, complex_selector)
            elements = browser.find_elements(By.CSS_SELECTOR, complex_selector)
            self.assertTrue(len(elements) == 1, "Should be only one element found with the selector")
            self.assertTrue(element.text == "Cat doesn't like bananas!", "'Cat doesn't like bananas!' description should be found with the selector")
        finally:
            browser.quit()

if __name__ == '__main__':
    unittest.main()
