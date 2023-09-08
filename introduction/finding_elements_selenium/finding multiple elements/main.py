from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    #test preparation
    # opening the page of the first merchandise item
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/")
    time.sleep(5)
    # adding the item to the cart
    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    add_button.click()

    # opening the page of the second item
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/")
    time.sleep(5)
    # adding the item to the cart
    add_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    add_button.click()

    # test scenario
    # opening the cart
    browser.get("http://selenium1py.pythonanywhere.com/en-gb/basket/")
    time.sleep(5)
    # searching for added items
    goods = browser.find_elements(By.CSS_SELECTOR, ".basket-items .row")

    # checking that the number of items equals 2
    assert len(goods) == 2
finally:
    browser.quit()