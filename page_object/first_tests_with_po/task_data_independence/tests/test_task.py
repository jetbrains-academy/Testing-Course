import unittest

import pytest
from _pytest.config import ExitCode


class TestCase(unittest.TestCase):
    def test_product_page(self):
        assert pytest.main(["test_product_page.py"]) == ExitCode.OK