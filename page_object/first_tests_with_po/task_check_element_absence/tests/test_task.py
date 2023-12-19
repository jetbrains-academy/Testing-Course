import unittest

import pytest
from _pytest.config import ExitCode


class TestCase(unittest.TestCase):
    def test_product_page(self):
        assert pytest.main(["test_product_page.py"]) == ExitCode.TESTS_FAILED

    def test_signatures(self):
        f = open("test_product_page.py", "r")
        text = f.read()
        assert "test_guest_cant_see_success_message_after_adding_product_to_basket" in text,\
            "No 'test_guest_cant_see_success_message_after_adding_product_to_basket' test"
        assert "test_guest_cant_see_success_message" in text,\
            "No 'test_guest_cant_see_success_message' test"
        assert "test_message_disappeared_after_adding_product_to_basket" in text,\
            "No 'test_message_disappeared_after_adding_product_to_basket' test"

