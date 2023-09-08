import unittest

import pytest
from _pytest.config import ExitCode


class TestCase(unittest.TestCase):
    def test_login_link(self):
        assert pytest.main(["test_main_page.py"]) == ExitCode.TESTS_FAILED
