'''
1. Navigate to: https://s3.amazonaws.com/capitalbikeshare-data/index.html.
2. Capture href elements in a list after they render.
3. Extract URLs for zip files from href elements.

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
ELEMENT_TYPE = "//a[@href]"
RETRY_COUNT = 5
ZIP_URL_LIST = []

def main():
    
    # 1. Navigate to: https://s3.amazonaws.com/capitalbikeshare-data/index.html.
    driver = page_navigator(MAIN_URL)

    # 2. Capture href elements in a list after they render.
    href_elements = element_grabber(driver, ELEMENT_TYPE)

    # 3. Extract URLs for zip files from href elements.
    zip_url_list = url_extractor(href_elements)

def page_navigator(url:str) -> webdriver:

    driver = webdriver.Chrome() 
    driver.set_page_load_timeout(10)
    driver.get(url)

    assert driver.current_url == 'https://s3.amazonaws.com/capitalbikeshare-data/index.html'
    
    logging.info(f'Successfully navigated to {driver.current_url}')

    return driver

def element_grabber(cbs_driver:webdriver, 
                    element_type:str) -> list:
    
    retries = RETRY_COUNT

    while retries > 0:

        try:
            WebDriverWait(cbs_driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '.zip'))).get_attribute('href')
            elements = cbs_driver.find_elements(By.XPATH, element_type)
            time.sleep(2)

            assert len(elements) > 0
            logging.info(f'Successfully found {element_type} elements at {MAIN_URL}')

            break

        except:
            time.sleep(2)
            retries = retries - 1
            logging.warning(f'Failed to find href elements at {MAIN_URL}')
            logging.warning(f'Retries remaining: {retries}')

    return elements

def url_extractor(href_list:list) -> list:

    for element in href_list:
        ZIP_URL_LIST.append(element.get_attribute('href'))

    assert len(ZIP_URL_LIST) > 0
    zip_url_count = len(ZIP_URL_LIST)
    logging.info(f'Successfully found {zip_url_count} zip file URLs at {MAIN_URL}')

    return ZIP_URL_LIST

if __name__=='__main__':
    main()