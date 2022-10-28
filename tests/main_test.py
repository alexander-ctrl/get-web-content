
from msilib.schema import SelfReg
from typing_extensions import Self
import unittest
from bs4 import BeautifulSoup
import requests, re

from main import search_emails, search_images, search_urls

class TestSum(unittest.TestCase):

    def __init__(Self):
        Self.URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        Self.URL_TEST = "/home/alexander/Documents/python-apps/get-web-content/index.html"
        reqs = requests.get(Self.URL_TEST)
        Self.soup = BeautifulSoup(reqs.text,'html.parser')
        

    def test_search_mails(Self):
        result = search_emails(Self.soup())
        Self.assertIsNotNone(result)
        Self.assertTrue(len)(result > 0);

    def test_search_url(Self):
        # Search URL IMAGES
        result = search_images(Self.soup)
        regex = Self.URL_REGEX
        isUrl = re.match(regex, result)
        Self.assertIsTrue(isUrl)

        # Search URL Pages
        result = search_urls(Self.soup)
        regex = Self.URL_REGEX
        isUrl = re.match(regex, result)
        Self.assertIsTrue(isUrl)


if __name__ == "__main__":
     unittest.main()