from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "https://suninjuly.github.io/explicit_wait2.html"


def wait_test(browser):
    def solve_quiz(browser):
        random_value = browser.find_element(By.ID, "input_value").text
        answer = (math.log(abs((12 * math.sin(float(random_value))))))
        text_field = browser.find_element(By.ID, "answer")
        text_field.send_keys(str(answer))
        browser.find_element(By.ID, "solve").click()

    browser.get(link)
    price_text = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element(By.ID, "book")
    button.click()

    solve_quiz(browser)
