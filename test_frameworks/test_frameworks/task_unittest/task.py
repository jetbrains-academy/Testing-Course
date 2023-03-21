from selenium import webdriver
import time
import unittest

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def register(link, browser):
    browser.get(link)

    browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys('Smolensk')

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    return welcome_text_elt.text
    browser.quit()


class TestLink(unittest.TestCase):

    def test_link1(self):
        browser = webdriver.Chrome()
        link1 = 'http://suninjuly.github.io/registration1.html'
        self.assertEqual(register(link1, browser), "Congratulations! You have successfully registered!")
        browser.quit()

    def test_link2(self):
        browser = webdriver.Chrome()
        link2 = 'http://suninjuly.github.io/registration2.html'
        self.assertEqual(register(link2, browser), "Congratulations! You have successfully registered!")
        browser.quit()

if __name__ == "__main__":
    unittest.main()
