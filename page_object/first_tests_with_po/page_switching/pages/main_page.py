from page_object.first_tests_with_po.page_switching.pages.base_page import BasePage
from page_object.first_tests_with_po.page_switching.pages.locators import *


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
