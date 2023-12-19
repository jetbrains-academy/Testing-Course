import unittest

import pytest
from _pytest.config import ExitCode


class TestCase(unittest.TestCase):
    def test_product_page(self):
        assert pytest.main(["test_product_page.py"]) == ExitCode.TESTS_FAILED

    def test_bug_report(self):
        f = open("bugreport.txt", "r")
        assert f.read() == "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", \
            "wrong bug report"
