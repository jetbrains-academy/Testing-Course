import unittest

from introduction.page_structure.task_attributes.task import *


class TestCase(unittest.TestCase):
    def test_add(self):
        correct = {
            "target": "for the <a> tag, it specifies how to open the link: in the current window or in a new one.",
            "src": "for the <img> tag specifies the source link of the image",
            "title": "basic attribute, specifies the tooltip text for element",
            "id": "basic attribute, specifies unique identifier for element on the page",
            "href": "specifies link address for the <a> tag"
        }
        res = correct == answer
        self.assertTrue(res, msg="Wrong answer")
