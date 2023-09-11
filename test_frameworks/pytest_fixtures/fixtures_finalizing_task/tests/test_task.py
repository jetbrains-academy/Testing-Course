import os
import unittest

import pytest
import time
import math


def check(reply):
    problem_number = 2105
    minutes_to_delay = 5

    ts_now = int(time.time())
    ts_past = ts_now - 60 * minutes_to_delay

    hashcode_now = math.log(ts_now * problem_number)
    hashcode_past = math.log(ts_past * problem_number)
    try:
        replys = float(reply)
        if (replys < hashcode_now and replys > hashcode_past):
            return True
        elif replys <= hashcode_past:
            return 0, "Срок действия кода истек, попробуйте еще раз"
        else:
            return 0, "Неверный код"

    except ValueError:
        return 0, "Неверный формат строки, должно быть число"


filename = "answer.txt"
newname = "answer1.txt"

class TestCase(unittest.TestCase):
    def test_script(self):
        pytest.main(["test_items.py"])
        assert not os.path.isfile(filename)


