from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    #test preparation
    # opening the page of the first merchandise item
    # the site does not exist, the code is just an example
    browser.get("https://fake-shop.com/book1.html")

    # adding the item to the cart
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # opening the page of the second item
    browser.get("https://fake-shop.com/book2.html")

    # adding the item to the cart
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()

    # test scenario
    # opening the cart
    browser.get("https://fake-shop.com/basket.html")

    # searching for added items
    goods = browser.find_elements(By.CSS_SELECTOR, ".good")

    # checking that the number of items equals 2
    assert len(goods) == 2
finally:
    browser.quit()