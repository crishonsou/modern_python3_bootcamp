### import library

from time import time
from functools import wraps

#### Define speed test decorator

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'Executing {fn.__name__}')
        print(f'Time Elapsed: {end_time - start_time:.4f}')
        return result
    return wrapper


### Definir a soma dos numeros usando o decorator criado

@speed_test
def sum_nums_list():
    return sum([x for x in range(50000000)])

@speed_test
def sum_nums_gen():
    return sum(x for x in range(50000000))


print(sum_nums_list())
print(sum_nums_gen())

    
        



