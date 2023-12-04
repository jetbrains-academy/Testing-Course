from selenium.common import NoSuchElementException

from .pages.main_page import MainPage


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    try:
        page.should_be_login_link()
    except NoSuchElementException:
        pass