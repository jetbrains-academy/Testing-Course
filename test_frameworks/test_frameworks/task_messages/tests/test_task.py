import unittest

from test_frameworks.test_frameworks.task_messages.task import test_input_text


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test1(self):
        try:
            test_input_text(8, 11)
        except AssertionError as e:
            self.assertEqual(str(e), "expected 8, got 11")
        else:
            self.fail('AssertionError not raised')

    def test2(self):
        test_input_text(11, 11)

    def test3(self):
        try:
            test_input_text(11, 15)
        except AssertionError as e:
            self.assertEqual(str(e), "expected 11, got 15")
        else:
            self.fail('AssertionError not raised')

    def test4(self):
        try:
            test_input_text("some_text", "text")
        except AssertionError as e:
            self.assertEqual(str(e), "expected some_text, got text")
        else:
            self.fail('AssertionError not raised')