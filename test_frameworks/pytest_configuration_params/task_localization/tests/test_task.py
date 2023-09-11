import sys
import unittest

import pytest
from pytest import ExitCode


class TestCase(unittest.TestCase):
    def test_espanol(self):
        assert pytest.main(["--language=es", "test_items.py"]) == ExitCode.OK

    def test_french(self):
        assert pytest.main(["--language=fr", "test_items.py"]) == ExitCode.OK

    def test_negative(self):
        assert pytest.main(["--language=fr",  "test_items_hidden.py"]) == ExitCode.OK

