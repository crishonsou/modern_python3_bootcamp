from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError('No Kwargs Allowed!')
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print('Hi there {name}')



greet(name='John')
        
