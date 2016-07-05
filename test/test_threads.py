"""
unit test here
create two spiders: MainSpider & BranchSpider
create a global Database
then push spiders to ThreadCreator, BOOM!
"""

from .spiders import MainSpider, BranchSpider
from .database import database_creator

from threads_creator import ThreadCreator, config_creator

URLS = [1, 2, 3]


def test_threads():
    config = config_creator()
    config.debug = 1
    config.main_sleep = (0, 1)
    config.branch_sleep = (0, 1)

    database = database_creator()
    thread_creator = ThreadCreator(main_spider=MainSpider, branch_spider=BranchSpider)
    thread_creator.get_entry_urls(urls=URLS)
    thread_creator.finish_all_threads()

    assert database is not None
    assert len(database.data) > 1

    print('all thread finished')
