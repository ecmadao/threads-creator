#!usr/env/bin python
import threading
from time import sleep
import random


class BranchThread(threading.Thread):
    __slots__ = ["branch_queue", "branch_spider"]

    def __init__(self, branch_queue=None, branch_spider=None):
        threading.Thread.__init__(self)
        self.branch_queue = branch_queue
        self.branch_spider = branch_spider

    def run(self):
        while 1:
            url = self.branch_queue.get()
            print('branch thread-{} start'.format(url))
            branch_spider = self.branch_spider(url)
            sleep(random.randrange(3, 10))
            branch_spider.request_page()
            print('branch thread-{} end'.format(url))
            self.branch_queue.task_done()


