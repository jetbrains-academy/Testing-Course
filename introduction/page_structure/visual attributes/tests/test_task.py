import unittest

from bs4 import BeautifulSoup


class TestCase(unittest.TestCase):
    def test_add(self):
        HTMLFile = open("index.html", "r")
        index = HTMLFile.read()
        HTMLFile.close()
        soup = BeautifulSoup(index, "html5lib")
        image = soup.img
        try:
            self.assertTrue(soup.h1["style"] == "color: blue;", f"Should be color: blue style, got {soup.h1['style']}")
            self.assertTrue("hidden" in str(soup.p), f"Should be hidden paragraph")
            self.assertTrue("disabled" in str(soup.button).split('>')[0], f"Should be disabled button")

        except Exception as e:
            self.fail("wrong page structure")
