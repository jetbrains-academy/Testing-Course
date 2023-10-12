import unittest

import pytest
from _pytest.config import ExitCode
from page_object.first_tests_with_po.elements.pages.locators import *


class TestCase(unittest.TestCase):
    def test_login_link(self):
        assert pytest.main(["test_main_page.py"]) == ExitCode.OK

    def test_locator(self):
        assert MainPageLocators.LOGIN_LINK == (By.CSS_SELECTOR, "#login_link")


