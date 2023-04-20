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
            self.assertTrue("picture" in image["class"], "Should be class 'picture' to image")
            self.assertTrue(image.src != "", "Should be source link to image")
            self.assertTrue(soup.div["name"] == "about", "Should be 'name' attribute with value 'about'")
            self.assertTrue(soup.div.h3["id"] == "pet-name", "Should be 'pet-name' id in header")
            self.assertTrue(soup.div.h3.text != "", "Should be pet name in header")
            self.assertTrue(soup.div.p.text != "", "Should be description")
            self.assertTrue(soup.div.p["data-type"] == "description", "Should be 'data-type'"
                                                                      " attribute with 'description value'")
        except Exception as e:
            self.fail("wrong page structure")