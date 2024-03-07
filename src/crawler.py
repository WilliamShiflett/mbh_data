from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Crawler:
    '''
    A webcrawler that:
      1.) Navigates to a URL
      2.) Waits for elements at the URL to render
      3.) Finds certain elements 
      4.) Checks the file types of those elements
      5.) Collects the urls to those files in a list
    '''
    def __init__(self, url, file_type, wait_time, attribute):
        self.url = url
        self.file_type = file_type
        self.wait_time = wait_time
        self.attribute = attribute

    def element_grabber(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(options=options)

        # Navigate to URL...
        driver.get(self. url)
        # Wait for elements to be clickable...
        WebDriverWait(driver, self.wait_time).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.file_type ))).get_attribute('href')
        # Gather elements in a list...
        self.elements = driver.find_elements(By.XPATH, self.attribute)
        # Clean-up time.
        driver.close()
        driver.quit()

        return self.elements

