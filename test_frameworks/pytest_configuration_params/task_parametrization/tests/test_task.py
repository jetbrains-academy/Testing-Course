import unittest

from test_frameworks.pytest_configuration_params.task_parametrization.answer import answer


# todo: replace this with an actual test
class TestCase(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(answer, "The owls are not what they seem! OvO", msg="wrong answer")
