'''
Detect new quarterly files on https://s3.amazonaws.com/capitalbikeshare-data/index.html
1.) Navigate to url
2.) Check for content
3.) Make hash of content
4.) Store hash of content
5.) Create cron job
6.) Run steps 1-4 at cron job interval
7.) Compare hashes to determine if website changed
8.) Download new file if website has changed
'''

#TO-DO: Figure out how to test retry counter

import pytest
import selenium.common.exceptions
from ..src.get_trip_zips import page_crawler, MAIN_URL

WRONG_URL = 'https://s3.amazon.aws.com/not_real/index.html'

#Is the webdriver going to the right URL? Is it active?
def test_right_url():
    page_crawler(MAIN_URL)

#What about the wrong URL?
def test_wrong_url():
    with pytest.raises(selenium.common.exceptions.WebDriverException):
        page_crawler(WRONG_URL)

#Are there zip files at the right URL?
def test_zip_files_at_url():
    test_elements = page_crawler(MAIN_URL)
    assert test_elements is not None