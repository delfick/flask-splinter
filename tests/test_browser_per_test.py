from base import BrowserTestCase

class TestThings(BrowserTestCase):
    def test_it_works(self):
        self.browser.visit("/")
        assert 'root' in self.browser.html

    def test_it_works_and_stuff(self):
        self.browser.visit("/")
        assert 'root' in self.browser.html
