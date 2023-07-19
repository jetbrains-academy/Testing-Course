import unittest

from introduction.finding_elements.find_elements_tag.task import answer


class TestCase(unittest.TestCase):
    def test_add(self):
        result = str(answer) == "7"
        self.assertTrue(result, msg="wrong answer")
