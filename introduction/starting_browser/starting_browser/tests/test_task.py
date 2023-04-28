import unittest

from introduction.starting_browser.starting_browser.task import first_script


class TestCase(unittest.TestCase):
    def test_add(self):
        first_script()
