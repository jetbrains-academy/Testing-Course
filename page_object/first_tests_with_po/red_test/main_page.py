from page_object.first_tests_with_po.base_page.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()