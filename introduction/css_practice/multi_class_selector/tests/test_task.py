import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from introduction.css_practice.multi_class_selector.task import multi_class_selector


class TestCase(unittest.TestCase):
    def test_script(self):
        self.assertFalse("body" in multi_class_selector, "Selector shouldn't contain 'body'")
        try:
            browser = webdriver.Chrome()
            browser.get("http://localhost:63342/UI%20test%20automation%20with%20Selenium%20and%20Python/introduction/css_practice/multi_class_selector/index.html?_ijt=dloj4gje1871ele4do3hc6i31a")
            element = browser.find_element(By.CSS_SELECTOR, multi_class_selector)
            elements = browser.find_elements(By.CSS_SELECTOR, multi_class_selector)
            self.assertTrue(len(elements) == 1, "Should be only one element found with the selector")
            self.assertTrue(element.text == "Watermelon story", "'Watermelon story' description should be found with the selector")
        finally:
            browser.quit()

if __name__ == '__main__':
    unittest.main()
