"""
unit test here
create two spiders: MainSpider & BranchSpider
create a global Database
then push spiders to ThreadCreator, BOOM!
"""

from .spiders.spider import MainSpider
from .spiders.spider import BranchSpider
from .database.database import database_creator

from spider_threads.entry import ThreadCreator

URLS = [1]


def test_threads():
    database = database_creator()
    thread_creator = ThreadCreator(main_spider=MainSpider, branch_spider=BranchSpider)
    thread_creator.get_entry_urls(urls=URLS)
    thread_creator.finish_all_threads()

    print('all thread finished')
    if database is not None:
        print(database.data)