import unittest

import pytest
from _pytest.config import ExitCode


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_product_page_go_to_login(self):
        assert pytest.main(["test_product_page.py::test_guest_can_go_to_login_page_from_product_page"]) == ExitCode.OK

    def test_product_page_should_be_login_link(self):
        assert pytest.main(["test_product_page.py::test_guest_should_see_login_link_on_product_page"]) == ExitCode.OK

    def test_signatures(self):
        f = open("test_product_page.py", "r")
        text = f.read()
        try:
            assert "should_be_login_link()" in text,\
                "No 'should_be_login_link' method invocation in test"
            assert "should_be_login_page()" in text, \
                "No 'should_be_login_page' method invocation in test"
        finally:
            f.close()

    def test_base_page(self):
        f = open("pages/base_page.py", "r")
        text = f.read()
        try:
            assert "should_be_login_link" in text,\
                "No 'should_be_login_link' method in base page"
        finally:
            f.close()