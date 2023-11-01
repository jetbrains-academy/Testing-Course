from selenium.common import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message(self, name, price):
        actual_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert name == actual_name, "Expected {}, got {}".format(name, actual_name)
        actual_price = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_PRICE).text
        assert price == actual_price, "Expected {}, got {}".format(price, actual_price)

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "No add to cart button"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
