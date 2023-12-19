import unittest

import pytest
from _pytest.config import ExitCode
from selenium.webdriver.common.by import By

from page_object.first_tests_with_po.task.pages.locators import MainPageLocators


class TestCase(unittest.TestCase):
    def test_login_link(self):
        assert pytest.main(["test_main_page.py"]) == ExitCode.OK

    def test_locator(self):
        assert MainPageLocators.LOGIN_LINK == (By.CSS_SELECTOR, "#login_link")


