import unittest

from introduction.page_structure.task_attributes_2.task import *


class TestCase(unittest.TestCase):
    def test_add(self):
        correct = {
            "required": "for the <input> tag specifies if the field is mandatory",
            "placeholder": "for the <input> tag adds text inside text field, that disappears when element in focus",
            "type": "for the <input> tag specifies what kind of information will be provided",
            "disabled": "for the <button> tag specifies if button is blocked for interaction"
        }
        res = correct == answer
        self.assertTrue(res, msg="Wrong answer")
