import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # initializing page object
    page.open()  # opening page
    page.go_to_login_page()  # using page method to open login page
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
    login_page.should_be_login_url()
    login_page.should_be_register_form()


@pytest.mark.xfail(raises=AssertionError, strict=True)
def test_guest_can_go_to_login_page_neg1(browser):
    login_page = LoginPage(browser, link)
    login_page.should_be_login_form()


@pytest.mark.xfail(raises=AssertionError, strict=True)
def test_guest_can_go_to_login_page_neg2(browser):
    login_page = LoginPage(browser, link)
    login_page.should_be_login_url()


@pytest.mark.xfail(raises=AssertionError, strict=True)
def test_guest_can_go_to_login_page_neg3(browser):
    login_page = LoginPage(browser, link)
    login_page.should_be_register_form()
