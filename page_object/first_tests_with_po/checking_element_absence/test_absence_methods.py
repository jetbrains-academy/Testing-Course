import pytest

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    expected_name = page.get_product_name()
    expected_price = page.get_product_price()
    page.should_be_success_message(expected_name, expected_price)


@pytest.mark.xfail(strict=True)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
