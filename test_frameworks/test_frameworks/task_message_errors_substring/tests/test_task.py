import unittest

from test_frameworks.test_frameworks.task_message_errors_substring.task import test_substring


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test1(self):
        try:
            test_substring("fulltext", "some_value")
        except AssertionError as e:
            self.assertEqual(str(e), "expected 'some_value' to be substring of 'fulltext'")
        else:
            self.fail('AssertionError not raised')

    def test2(self):
        test_substring("111", "1")

    def test3(self):
        test_substring("1", "1")

    def test4(self):
        try:
            test_substring("http://suninjuly.github.io/registration1.html", "login")
        except AssertionError as e:
            self.assertEqual(str(e), "expected 'login' to be substring of 'http://suninjuly.github.io/registration1.html'")
        else:
            self.fail('AssertionError not raised')

    def test5(self):
        test_substring("some_text", "some")