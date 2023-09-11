from selenium.webdriver.common.by import By

from page_object.first_tests_with_po.base_page.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу     # выполняем метод страницы — переходим на страницу логина
    assert browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary.btn-block").text == "Add to basket"