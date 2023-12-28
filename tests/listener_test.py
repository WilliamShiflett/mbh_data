import bs4
import pytest
from ..src.listener import page_getter, URL
from http import HTTPStatus

#are the zip files there?
def test_rendered_page_clickable_zip():
    test_zip = page_getter(URL)
    assert test_zip is not None
