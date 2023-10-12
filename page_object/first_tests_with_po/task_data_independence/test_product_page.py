import math
from selenium.common.exceptions import NoAlertPresentException

from page_object.first_tests_with_po.task_add_item.pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    expected_name = page.get_product_name()
    expected_price = page.get_product_price()
    page.should_be_success_message(expected_name, expected_price)



