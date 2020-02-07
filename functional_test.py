from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.newBrowser = webdriver.Firefox()

    def tearDown(self):
        self.newBrowser.quit()

    def test_canStartAListAndRetrieveItLater(self):
        self.newBrowser.get("http://localhost:8000")
        self.assertIn("To-Do", self.newBrowser.title)
        self.fail("Finish the test.")

    # ...


if __name__ == '__main__':
    unittest.main(warnings='ignore')
