#!usr/bin/env python
"""
SPIDER THREADS
thread creator
here we create several main-thread
"""
import queue
from .config import config_creator
from .utils import error_message, VALIDATE_URLS
# from .utils.message import error_message
# from .utils.const_value import VALIDATE_URLS
# from .threads.main_thread import MainThread
from .threads import MainThread


class ThreadCreator(object):
    __slots__ = ["main_thread_number",
                 "main_queue",
                 "main_spider",
                 "branch_spider",
                 "debug"]

    def __init__(self, main_spider=None, branch_spider=None):
        config = config_creator()
        main_thread_number = config.main_thread_num
        self.main_thread_number = main_thread_number
        self.main_queue = queue.Queue(main_thread_number)
        self.main_spider = main_spider
        self.branch_spider = branch_spider
        self.debug = config.debug

    def get_entry_urls(self, urls=list()):
        """

        :param urls: url you want to fetch
        :return: None
        """
        try:
            assert type(urls) in VALIDATE_URLS
        except AssertionError:
            error_message('urls should be a list or tuple')
        if len(urls):
            for i in range(self.main_thread_number):
                self.append_main_thread()

            for url in urls:
                self.main_queue.put(url)
        else:
            error_message('it is an empty list/tuple')

    def append_main_thread(self):
        """create & start main thread

        :return: None
        """
        thread = MainThread(main_queue=self.main_queue,
                            main_spider=self.main_spider,
                            branch_spider=self.branch_spider)
        thread.daemon = True
        thread.start()

    def finish_all_threads(self):
        self.main_queue.join()
        if self.debug:
            print('all main thread is finish')

