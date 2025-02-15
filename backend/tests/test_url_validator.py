import unittest
from app.url_validator import is_valid_url

class TestURLValidation(unittest.TestCase):
    def test_valid_urls(self):
        valid_urls = [
            "http://foo.com",
            "https://foo.com",
            "http://foo.bar.com",
            "https://foo.com:8080/bar"
        ]
        for url in valid_urls:
            with self.subTest(url=url):
                self.assertTrue(is_valid_url(url))
    
    def test_invalid_urls(self):
        invalid_urls = [
            "foo", "http:/foo.com", "htt://foo.com", "foo.com", "http://"
        ]
        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertFalse(is_valid_url(url))