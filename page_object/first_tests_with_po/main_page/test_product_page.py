import math
from selenium.common.exceptions import NoAlertPresentException

from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    expected_name = page.get_product_name()
    expected_price = page.get_product_price()
    page.should_be_success_message(expected_name, expected_price)



