from .utils.message import error_message

config = None


def config_creator():
    global config
    if config is None:
        config = {
            'main_thread_num': 5,
            'main_thread_sleep': (1, 3),
            'branch_thread_num': 3,
            'branch_thread_sleep': (1, 3)
        }
    return config


def assert_agr_is_num(arg):
    num = None
    try:
        assert type(arg) in (int, str)
        num = int(arg)
    except (AssertionError, ValueError):
        error_message('except a number')
    finally:
        return num


def set_thread_num(num, config_type):
    result = assert_agr_is_num(num)
    if result:
        config_dict = config_creator()
        config_dict[config_type] = result


def set_thread_sleep_time(start_time, end_time, config_type):
    start_time = assert_agr_is_num(start_time)
    end_time = assert_agr_is_num(end_time)
    if start_time & end_time:
        config_dict = config_creator()
        config_dict[config_type] = (start_time, end_time)


def set_main_thread_num(num):
    set_thread_num(num, 'main_thread_num')


def set_main_thread_sleep(start_time=1, end_time=3):
    set_thread_sleep_time(start_time, end_time, 'main_thread_sleep')


def set_branch_thread_num(num):
    set_thread_num(num, 'branch_thread_num')


def set_branch_thread_sleep(start_time=1, end_time=3):
    set_thread_sleep_time(start_time, end_time, 'branch_thread_sleep')
