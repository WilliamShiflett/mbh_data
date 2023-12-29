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
import boto3
import json
import time
import hashlib
import requests
from http import HTTPStatus
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://s3.amazonaws.com/capitalbikeshare-data/index.html'

def page_getter(url: str):
    driver = webdriver.Chrome() 
    driver.get(url)
    #Implement max retries
    try:
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '.zip'))).get_attribute('href')
        elems = driver.find_elements(By.XPATH, "//a[@href]")
        time.sleep(5)
    except:
        time.sleep(5)
    
    return elems

def main():
    # test = page_getter(URL)
    # for e in test:
    #     print(e.get_attribute('href'))
    import requests, zipfile, io
    r = requests.get('https://s3.amazonaws.com/capitalbikeshare-data/202112-capitalbikeshare-tripdata.zip')
    z = zipfile.ZipFile(io.BytesIO(r.content))
    print(z.namelist())

if __name__=='__main__':
    main()