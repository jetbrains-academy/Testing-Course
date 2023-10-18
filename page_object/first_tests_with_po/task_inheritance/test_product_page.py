import pytest

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
        "Success message is presented, but should not be"


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
        "Success message is presented, but should not be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
        'Success message isnt disappeared'


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # initializing page object
    page.open()  # opening page
    page.go_to_login_page()  # using page method to open login page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
