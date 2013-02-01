from base import BrowserRunner
import unittest

browser, setup, teardown = BrowserRunner.as_fixture()

class TestThings(unittest.TestCase):
    def setUp(self):
        self.browser = browser

    def test_it_works(self):
        self.browser.visit("/lol?num=1")
        assert 'lol1' in self.browser.html

    def test_it_works2(self):
        self.browser.visit("/lol?num=2")
        assert 'lol2' in self.browser.html

    def test_it_works3(self):
        self.browser.visit("/lol?num=3")
        assert 'lol3' in self.browser.html

    def test_some_javascript(self):
        self.browser.visit("/some_javascript")
        assert '<p>clicked</p>' not in self.browser.html
        self.browser.find_by_id("clicker").click()
        assert '<p>clicked</p>' not in self.browser.html
