''' 
1. Navigate to: https://s3.amazonaws.com/capitalbikeshare-data/index.html.
2. Capture href elements in a list after they render.
3. Extract URLs for zip files from href elements.
'''

import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import logging
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, TimeoutException
import unittest

from src.crawler import Crawler

# Set up log file. Remeber to add to .gitignore.

logging.basicConfig(level=logging.DEBUG,
                    filename="mbh_data_crawler_test_log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')

# Globabl variables. Do not change.

URL = "https://s3.amazonaws.com/capitalbikeshare-data/index.html"
ATTRIBUTE = "//a[@href]"
WAIT_TIME = 2
FILE_TYPE = ".zip"
RETRY_COUNT = 3

WRONG_URL = "www.google.com"
# WRONG_LINK_TEXT = 
# WRONG_ATTRIBUTE = 
# WRONG_WAIT_TIME = 
# WRONG_FILE_TYPE = 
# WRONG_RETRY_COUNT = 

class DriverTestCase(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.test_webdriver = webdriver.Chrome(options=options)
        self.test_url = URL

    def test_HaveChromeBrowser(self):
        # Do we have the Chrome browser?
        self.assertEqual(self.test_webdriver.current_url,"data:,")

    def test_CanAccessURL(self):
        # Can we access the correct URL from wherever this is installed?
        self.test_webdriver.get(self.test_url)
        self.assertEqual(self.test_webdriver.current_url, URL)
    
    def tearDown(self):
        self.test_webdriver.close()
        self.test_webdriver.quit()

class CrawlerExpectedTestCase(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler(url=URL, 
                               file_type=FILE_TYPE,
                               wait_time=WAIT_TIME,
                               attribute=ATTRIBUTE)

    def test_CrawlerExists(self):
        self.assertIsNotNone(self.crawler)

    def test_CrawlerHasURL(self):
        self.assertIsNotNone(self.crawler.url)

    def test_CrawlerURLIsString(self):
        self.assertIsInstance(self.crawler.url, str)

    def test_CrawlerURLWebsiteOk(self):
        response = requests.get(self.crawler.url)
        self.assertEqual(response.status_code, 200)

    def test_CrawlerURLWebsiteHasTemplate(self):
        response = requests.get(self.crawler.url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.text)

    def test_CrawlerHasFileType(self):
        self.assertIsNotNone(self.crawler.file_type)

    def test_CrawlerFileTypeIsString(self):
        self.assertIsInstance(self.crawler.file_type, str)

    def test_CrawlerHasWaitTime(self):
        self.assertIsNotNone(self.crawler.wait_time)

    def test_CrawlerWaitTimeIsNonZeroIntegr(self):
        self.assertIsInstance(self.crawler.wait_time, int)
        self.assertGreater(self.crawler.wait_time, 0)

    def test_CrawlerCanNavigateAndWait(self):
        self.crawler.element_grabber()

    def test_CrawlerCanFindElements(self):
        elements = self.crawler.element_grabber()
        self.assertIsNotNone(elements)

class CrawlerUnexpectedTestCase(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler(url=WRONG_URL, 
                               file_type=FILE_TYPE,
                               wait_time=WAIT_TIME,
                               attribute=ATTRIBUTE)
        
    def test_NoURL(self):
        with self.assertRaises(TimeoutException):
            self.crawler.element_grabber()

if __name__ == "__main__":
    unittest.main()