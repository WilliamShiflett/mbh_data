import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import logging
import requests
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, TimeoutException
import unittest

from src.get_trip_zips import page_navigator

# Set up log file. Remeber to add to .gitignore.

logging.basicConfig(level=logging.DEBUG,
                    filename="get_trip_zips_test_log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S')

# Globabl variables. Do not change.

URL = "https://s3.amazonaws.com/capitalbikeshare-data/index.html"
ATTRIBUTE = "//a[@href]"
WAIT_TIME = 2
FILE_TYPE = ".zip"
RETRY_COUNT = 3

class test_page_navigator(unittest.TestCase):

    def test_PageIsUp(self):
        response = requests.head(URL)
        self.assertEqual(response.status_code, 200)

    def test_FakeSiteNoWait(self):
        with self.assertRaises((InvalidArgumentException,TimeoutException)):
            self.assertIsNone(page_navigator(url="www.test.fake.url", 
                                             wait_time=0))

    def test_FakeSiteRealWait(self):
        with self.assertRaises((InvalidArgumentException)):
            self.assertIsNone(page_navigator(url="www.test.fake.url", 
                                             wait_time=WAIT_TIME))
	
    def test_RealSiteNoWait(self):
        with self.assertRaises((TimeoutException)):
            self.assertIsNone(page_navigator(url=URL, 
                                             wait_time=0))
            
    def test_RealSiteRealWait(self):
        self.assertIsNotNone(page_navigator(url=URL, 
                                        wait_time=WAIT_TIME))
		
if __name__=='__main__':
	unittest.main()