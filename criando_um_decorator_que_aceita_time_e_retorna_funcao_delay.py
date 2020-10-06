from functools import wraps
from time import sleep


def delay(timer):
    def inner(fn):
        def wrapper(*args, **kwargs):
            print(f'Waiting {timer} seconds before runnig {fn.__name__}')
            sleep(timer)
            return fn(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hi():
    return 'hi'


print(say_hi())
            
            
