from functools import wraps

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable
            new_args =[]
            for (a, t) in zip(args, types):
                new_args.append(t(a))
            return f(*new_args, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_message(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    return a / b


repeat_message("hello", '3')
print(divide(10.5, 2.5))
