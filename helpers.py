import time


def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        finish = time.time()
        print(finish - start)
        return res

    return wrapper
