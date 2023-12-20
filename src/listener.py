'''
Detect new quarterly files on https://s3.amazonaws.com/capitalbikeshare-data/index.html
1.) Navigate to url
2.) Check for content
3.) Make hash of content
4.) Store hash of content
5.) Create cron job
6.) Run steps 1-4 at cron job interval
7.) Compare hashes to determine if website changed
8.) Use downloader.py if website has changed
'''

import json
import time
import hashlib
import requests
from http import HTTPStatus
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 




URL = 'https://s3.amazonaws.com/capitalbikeshare-data/index.html'

def requester(url: str):
    response = requests.get(url)
    return response

def texter(url_response):
    url_text = url_response.text
    return url_text

#above won't work due to page not rendering
    
# try visiting with selenium

def visitor(url: str):
    driver = webdriver.Chrome(ChromeDriverManager().install()) 
    driver.get(url)
    page = driver.page_source.encode('utf-8') 
    print(page)


    
def main():
    text_getter_input = requester(URL)
    text_getter_output = texter(text_getter_input)
    visitor(URL)

if __name__=='__main__':
    main()