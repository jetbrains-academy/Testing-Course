import unittest
import pytest


class TestCase(unittest.TestCase):
    def test_answer(self):
        pytest.main(["-s", "test_task.py"])
        f = open("answer.txt")
        reply = f.readline()
        try:
            assert reply == "penguins bake cookies, penguins eagerly feasting together "
        finally:
            f.close()