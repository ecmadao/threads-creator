# from .spiders.spider import MainSpider
# from .spiders.spider import BranchSpider

from spider_threads.entry import ThreadCreator

urls = [1]

database = None


def database_creator():
    global database
    if database is None:
        database = DataBase()


class DataBase(object):
    def __init__(self):
        self.data = []

    def append_date(self, data):
        self.data.append(data)


class MainSpider(object):
    def __init__(self, url):
        self.url = url
        print('main spider {} start!'.format(url))

    def request_urls(self):
        return ['{}-{}'.format(self.url, i) for i in range(3)]


class BranchSpider(object):
    def __init__(self, url):
        self.url = url
        print('branch spider {} start!'.format(url))

    def request_page(self):
        database.append_date('{}-object'.format(self.url))


def test_threads():
    database_creator()
    thread_creator = ThreadCreator(main_spider=MainSpider, branch_spider=BranchSpider)
    thread_creator.get_entry_urls(urls=urls)
    thread_creator.finish_all_threads()

    print('all thread finished')
    if database is not None:
        print(database.data)


test_threads()
