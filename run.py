#!usr/bin/env python
"""
SPIDER THREADS
"""

from utils.message import colorful_text, error_message
from utils.const_value import VALIDATE_URLS


def get_entry_urls(urls):
    assert type(urls) in VALIDATE_URLS
    if len(urls):
        pass
    else:
        error_message('it is a empty list/tuple')
