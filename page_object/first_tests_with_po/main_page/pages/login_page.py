from selenium.webdriver.common.by import By

from page_object.first_tests_with_po.login_page.pages.base_page import BasePage
from page_object.first_tests_with_po.login_page.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "/accounts/login/" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
