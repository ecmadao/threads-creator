# from .utils.message import error_message
from .utils import error_message

config = None


def config_creator():
    global config
    if config is None:
        config = Config()
    return config


class Config(object):
    def __init__(self):
        self.main_thread_num = 5
        self.main_thread_sleep = (1, 3)
        self.branch_thread_num = 3
        self.branch_thread_sleep = (1, 3)
        self.is_debug = 0

    @property
    def main_num(self):
        return self.main_thread_num

    @main_num.setter
    def main_num(self, num):
        num = Config.assert_agr_is_num(num)
        if num:
            self.main_thread_num = num

    @property
    def main_sleep(self):
        return self.main_thread_sleep

    @main_sleep.setter
    def main_sleep(self, times):
        start_time, end_time = times
        start_time = Config.assert_agr_is_num(start_time)
        end_time = Config.assert_agr_is_num(end_time)
        if start_time and end_time:
            self.main_thread_sleep = (start_time, end_time)

    @property
    def branch_num(self):
        return self.branch_thread_num

    @branch_num.setter
    def branch_num(self, num):
        num = Config.assert_agr_is_num(num)
        if num:
            self.branch_thread_num = num

    @property
    def branch_sleep(self):
        return self.branch_thread_sleep

    @branch_sleep.setter
    def branch_sleep(self, times):
        start_time, end_time = times
        start_time = Config.assert_agr_is_num(start_time)
        end_time = Config.assert_agr_is_num(end_time)
        if start_time and end_time:
            self.branch_thread_sleep = (start_time, end_time)

    @property
    def debug(self):
        return self.is_debug

    @debug.setter
    def debug(self, is_debug):
        self.is_debug = is_debug

    @staticmethod
    def assert_agr_is_num(arg):
        num = None
        try:
            assert type(arg) in (int, str)
            num = int(arg)
        except (AssertionError, ValueError):
            error_message('except a number')
        finally:
            return num
