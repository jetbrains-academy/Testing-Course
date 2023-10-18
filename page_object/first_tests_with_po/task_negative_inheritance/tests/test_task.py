import unittest

import pytest
from _pytest.config import ExitCode


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_main_page(self):
        assert pytest.main(["test_main_page.py::test_guest_cant_see_product_in_basket_opened_from_main_page"]) == ExitCode.OK

    def test_product_page(self):
        assert pytest.main(["test_product_page.py::test_guest_cant_see_product_in_basket_opened_from_product_page"]) == ExitCode.OK

    def test_signatures(self):
        f = open("test_product_page.py", "r")
        text = f.read()
        try:
            assert "should_be_empty_basket()" in text,\
                "No 'should_be_empty_basket' method invocation in test"
            assert "should_be_message_empty_basket()" in text, \
                "No 'should_be_message_empty_basket' method invocation in test"
        finally:
            f.close()

    def test_signatures_main_page(self):
        f = open("test_main_page.py", "r")
        text = f.read()
        try:
            assert "should_be_empty_basket()" in text,\
                "No 'should_be_empty_basket' method invocation in test"
            assert "should_be_message_empty_basket()" in text, \
                "No 'should_be_message_empty_basket' method invocation in test"
        finally:
            f.close()
