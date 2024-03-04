''' 
1. Navigate to: https://s3.amazonaws.com/capitalbikeshare-data/index.html.
2. Capture href elements in a list after they render.
3. Extract URLs for zip files from href elements.
'''

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

import unittest

from src.crawler import Crawler

URL = "https://s3.amazonaws.com/capitalbikeshare-data/index.html"
LINK_TEXT = ".zip"
ATTRIBUTE = "//a[@href]"
WAIT_TIME = 10
FILE_TYPE = ".zip"
RETRY_COUNT = 3

class CrawlerTestCase(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler(url=URL, 
                               file_type=FILE_TYPE,)

    def test_CrawlerExists(self):
        self.assertIsNotNone(self.crawler)

    def test_CrawlerHasURL(self):
        self.assertIsNotNone(self.crawler.url)

    def test_CrawlerURLIsString(self):
        self.assertIsInstance(self.crawler.url, str)

    def test_CrawlerURLWebsiteOk(self):
        response = requests.get(self.crawler.url)
        self.assertEquals(response.status_code, 200)

    def test_CrawlerURLWebsiteHasTemplate(self):
        response = requests.get(self.crawler.url)
        self.assertEquals(response.status_code, 200)
        self.assertIsNotNone(response.text)

    def test_CrawlerHasFileType(self):
        self.assertIsNotNone(self.crawler.file_type)

    def test_CrawlerFileTypeIsString(self):
        self.assertIsInstance(self.crawler.file_type, str)

    def test_CrawlerCanClick(self):
        # create webdriver object
        driver = webdriver.Chrome()
        driver.get(self.crawler.url)
        element = driver.find_element(By.LINK_TEXT, self.crawler.file_type)
        self.assertIsNotNone(element)
        # click the element
        element.click()

    # def test_CrawlerHasWaitTime(self):
    #     self.assertIsNotNone(self.crawler.wait_time)

    # def test_CrawlerWaitTimeIsNonZeroIntegr(self):
    #     self.assertIsInstance(self.crawler.wait_time, int)
    #     self.assertGreater(self.crawler.wait_time, 0)


    # def tearDown(self):
    #     self.crawler.something()

if __name__ == "__main__":
    unittest.main()

# For example you have a test that requires items to exist, 
# or certain state - so you put these actions
# (creating object instances, initializing db, preparing rules and so on) 
#into the setUp.

# Also as you know each test should stop in the place where 
# it was started - this means that we have to restore app state
# to it's initial state - 
# e.g close files, connections, removing newly created items, calling transactions callback and so on - all these steps are to be included into the tearDown.