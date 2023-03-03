import unittest

from test_frameworks.test_frameworks.task_unittest import answer


class TestCase(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(answer.answer, "FAILED (errors=1)", msg="wrong report format")
