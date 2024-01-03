'''
Navigate to:
https://s3.amazonaws.com/capitalbikeshare-data/index.html

Get zip file URLs for each quarter's worth of trip data.

'''
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

MAIN_URL = 'https://s3.amazonaws.com/capitalbikeshare-data/index.html'
RETRY_COUNT = 5
ZIP_URL_LIST = []

def page_crawler(url: str) -> list:
    '''
    1.Visits url
    2.Waits for href elements to render
    3.Finds all href elements
    4.Returns URLs in href elements
    '''

    driver = webdriver.Chrome() 
    driver.get(url)
    driver.set_page_load_timeout(20)

    assert driver.current_url == 'https://s3.amazonaws.com/capitalbikeshare-data/index.html'
    logging.info(f'Successfully got {driver.current_url}')

    retries = RETRY_COUNT
    while retries > 0:

        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '.zip'))).get_attribute('href')
            elements = driver.find_elements(By.XPATH, "//a[@href]")
            time.sleep(2)
            assert len(elements) > 0 
            break

        except:
            time.sleep(2)
            retries = retries - 1
            logging.warning(f'Failed to access {url}')
            logging.warning(f'Retries remaining: {retries}')
    
    for element in elements:
        ZIP_URL_LIST.append(element.get_attribute('href'))

    return ZIP_URL_LIST

def main():
    page_crawler(MAIN_URL)

if __name__=='__main__':
    main()