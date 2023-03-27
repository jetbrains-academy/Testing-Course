import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from introduction.css_practice.id_selectors.task import id_selector


class TestCase(unittest.TestCase):
    def test_script(self):
        self.assertFalse("body" in id_selector)
        try:
            browser = webdriver.Chrome()
            browser.implicitly_wait(4)
            browser.get("https://suninjuly.github.io/css-tasks/practice-id")
            element = browser.find_element(By.CSS_SELECTOR, id_selector)
            self.assertTrue(element.text == "Polite cat")
        finally:
            browser.quit()

if __name__ == '__main__':
    unittest.main()
