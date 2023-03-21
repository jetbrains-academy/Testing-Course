from selenium import webdriver


browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")
browser.quit()
