#!usr/env/bin python
database = None


def database_creator():
    """make sure you have only one instance of Database

    :return: DataBase's instance
    """
    global database
    if database is None:
        database = Database()
    return database


class Database(object):
    def __init__(self):
        self.data = []

    def append_data(self, data):
        self.data.append(data)
