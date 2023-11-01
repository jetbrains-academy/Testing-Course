from .pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)   # initializing page object
    page.open()                      # opening page
    page.go_to_login_page()          # using page method to open login page
