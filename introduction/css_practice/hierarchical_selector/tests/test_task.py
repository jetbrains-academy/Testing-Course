import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from introduction.css_practice.hierarchical_selector.task import hierarchical_selector


class TestCase(unittest.TestCase):
    def test_script(self):
        self.assertFalse("body" in hierarchical_selector, "Selector shouldn't contain 'body'")
        self.assertTrue(":nth-child(2)" in hierarchical_selector, "Selector should be hierarchical")
        try:
            browser = webdriver.Chrome()
            browser.get("http://localhost:63342/UI%20test%20automation%20with%20Selenium%20and%20Python/introduction/css_practice/hierarchical_selector/index.html?_ijt=js1r8brc28q5t58ifg9lgascii&_ij_reload=RELOAD_ON_SAVE")
            element = browser.find_element(By.CSS_SELECTOR, hierarchical_selector)
            elements = browser.find_elements(By.CSS_SELECTOR, hierarchical_selector)
            self.assertTrue(len(elements) == 1, "Should be only one element found with the selector")
            self.assertTrue(element.text == "Edit", "Edit' button should be found with the selector")
        finally:
            browser.quit()

if __name__ == '__main__':
    unittest.main()
