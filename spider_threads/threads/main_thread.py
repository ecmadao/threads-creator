#!usr/env/bin python
import threading
from time import sleep
import random
import queue
from .branch_thread import BranchThread
from ..utils.const_value import VALIDATE_URLS
from ..utils.message import error_message

existed_urls_list = []


class MainThread(threading.Thread):
    __slots__ = ['main_queue', 'main_spider', 'branch_spider']

    def __init__(self, main_queue, main_spider, branch_spider):
        threading.Thread.__init__(self)
        self.main_queue = main_queue
        self.main_spider = main_spider
        self.branch_spider = branch_spider

    def run(self):
        global existed_urls_list
        while 1:
            url = self.main_queue.get()
            print('main thread-{} start'.format(url))
            main_spider = self.main_spider(url)
            sleep(random.randrange(2, 5))
            links = main_spider.request_urls()

            try:
                assert type(links) in VALIDATE_URLS
            except AssertionError:
                error_message('except to return a list or tuple which contains url')

            branch_queue = queue.Queue(3)

            for i in range(2):
                branch_thread = BranchThread(branch_queue=branch_queue,
                                             branch_spider=self.branch_spider)
                branch_thread.daemon = True
                branch_thread.start()

            for link in links:
                if link not in existed_urls_list:
                    existed_urls_list.append(link)
                    branch_queue.put(link)

            branch_queue.join()
            print('main thread-{}\'s child threads is all finish'.format(url))
            self.main_queue.task_done()
