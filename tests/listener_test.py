import pytest
from src.listener import requester
from http import HTTPStatus

def test_url():
    test_status = requester('https://s3.amazonaws.com/capitalbikeshare-data/index.html')
    assert test_status.status_code == HTTPStatus.OK.value