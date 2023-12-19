import time

import pytest

from .pages.login_page import LoginPage


@pytest.mark.xfail(strict=True)
def test_auth_user_negative(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.should_be_authorized_user()


def test_auth_user_positive(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(str(time.time()) + "@fakemail.org", 'enigma123456')
    page.should_be_authorized_user()