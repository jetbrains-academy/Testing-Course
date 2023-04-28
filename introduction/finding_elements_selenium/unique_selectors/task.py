from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"


def finding_unique_selectors(browser):
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
    input3.send_keys("Smolensk")
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    time.sleep(1)
    assert "Congratulations! You have successfully registered!" == browser.find_element(By.TAG_NAME, "h1").text
