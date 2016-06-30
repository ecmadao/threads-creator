class MainSpider(object):
    def __init__(self, url):
        self.url = url
        print('main spider {} start!'.format(url))

    def request_urls(self):
        return ['{}-{}'.format(self.url, i) for i in range(5)]


class BranchSpider(object):
    def __init__(self, url):
        self.url = url
        print('branch spider {} start!'.format(url))

    def request_page(self):
        return '{}-object'.format(self.url)
