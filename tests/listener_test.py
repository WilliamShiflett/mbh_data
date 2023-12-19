import pytest
from src.listener import requester, texter
from http import HTTPStatus

#is this url still active?
def test_url():
    test_status = requester('https://s3.amazonaws.com/capitalbikeshare-data/index.html')
    assert test_status.status_code == HTTPStatus.OK.value

#is there anything at this url?
def test_url_text():
    test_url_response = requester('https://s3.amazonaws.com/capitalbikeshare-data/index.html')
    test_status = texter(test_url_response)
    assert test_status is not None

#can I make a hasg of what's at this url?

