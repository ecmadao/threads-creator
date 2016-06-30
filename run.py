#!usr/bin/env python
"""
SPIDER THREADS
"""
import queue
from utils.message import colorful_text, error_message
from utils.const_value import VALIDATE_URLS
from threads.main_thread import MainThread


# def get_entry_urls(urls):
#     assert type(urls) in VALIDATE_URLS
#     if len(urls):
#         pass
#     else:
#         error_message('it is a empty list/tuple')


class ThreadCreator(object):
    def __init__(self, main_spider, branch_spider, main_queue_number=5):
        self.main_queue = queue.Queue(main_queue_number)
        self.main_spider = main_spider
        self.branch_spider = branch_spider

    def get_entry_urls(self, urls):
        assert type(urls) in VALIDATE_URLS
        if len(urls):
            for url in urls:
                self.append_main_thread(self.main_spider)
            pass
        else:
            error_message('it is a empty list/tuple')

    @staticmethod
    def append_main_thread(main_spider):
        pass
