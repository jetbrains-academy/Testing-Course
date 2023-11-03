import unittest

import pytest
from _pytest.config import ExitCode


class TestCase(unittest.TestCase):
    def test_product_page(self):
        assert pytest.main(["test_product_page.py::TestUserAddToBasketFromProductPage::test_user_can_add_product_to_basket"]) == ExitCode.OK
        assert pytest.main(["test_product_page.py::test_guest_can_add_product_to_basket"]) == ExitCode.OK
        assert pytest.main(["test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page"]) == ExitCode.OK
        assert pytest.main(["test_product_page.py::test_guest_can_go_to_login_page_from_product_page"]) == ExitCode.OK


    def test_main_page(self):
        assert pytest.main(["test_main_page.py"]) == ExitCode.OK

    def test_registration_method(self):
        assert pytest.main(["test_util.py"]) == ExitCode.OK
