from selenium.webdriver.common.by import By

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()  # открываем страницу     # выполняем метод страницы — переходим на страницу логина
    assert browser.find_element(By.NAME, "login_submit").text == "Log In"
