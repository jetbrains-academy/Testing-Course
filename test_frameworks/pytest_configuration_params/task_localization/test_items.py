import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def link():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_have_button_add_to_basket(browser, link):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-add-to-basket").click()
    browser.find_element(By.CLASS_NAME, "alertinner")
