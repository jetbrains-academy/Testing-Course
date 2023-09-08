from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

browser.find_element(By.TAG_NAME, "select").click()
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()