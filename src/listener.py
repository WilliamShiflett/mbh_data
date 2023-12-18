'''Function to detect new quarterly files on https://s3.amazonaws.com/capitalbikeshare-data/index.html'''

import time
import hashlib
import requests
from http import HTTPStatus

URL = 'https://s3.amazonaws.com/capitalbikeshare-data/index.html'

def requester(url):
    response = requests.get(url)
    print(response)

def main():
    requester(URL)

if __name__=='__main__':
    main()