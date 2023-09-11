import pytest

from test_frameworks.pytest_configuration_params.task_localization import test_items
from selenium.webdriver.common.by import By


@pytest.mark.xfail(strict=True)
def test_negative(browser):
    test_items.test_is_have_button_add_to_basket(browser,
                                                 "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-cathedral-the-bazaar_190/")


def test_french(browser):
    test_items.test_is_have_button_add_to_basket(browser,
                                                 "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element(By.CLASS_NAME, "btn-add-to-basket").text == "Ajouter au panier"
