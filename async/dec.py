from time import time

def time_measure(func):

    def warpper(*args, **kwargs):
        start_time = time()
        t = func(*args, **kwargs)
        end_time = time()
        print(f"start: {start_time}, end: {end_time}, delta: {end_time - start_time}")
        return t
    return warpper






