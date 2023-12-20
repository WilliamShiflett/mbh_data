import pytest
from src.listener import requester, texter, visiter, URL
from http import HTTPStatus

#is this url still active?
def test_url():
    test_status = requester(URL)
    assert test_status.status_code == HTTPStatus.OK.value

#is there anything at this url?
def test_url_text():
    test_url_response = requester(URL)
    test_status = texter(test_url_response)
    assert test_status is not None

#can I make a hash of what's at this url?
def test_rendered_page():
    test_page = visiter(URL)
    assert visiter is not None



    
#will hash change moment by moment?


