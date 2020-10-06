# Podemos passar funções como argumentos para outras funções

def sum(n, func):
    total = 0
    for num in range(n):
        total += func(num)
    return total

def square(x):
    return x * x        

def cube(x):
    return x * x * x

print(sum(10, square))

print(sum(10, cube))


# Outro exemplo

from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello ', 'Hello There ', 'Go Away ', 'I Love You '))
        return msg
    result = get_mood() + person
    return result

print(greet('Toby'))


# Podemos retornar funções de outras funções

def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHA', 'LOL', 'HEHEHE', 'AHUSHAUSHUAS'))
        return l
    return get_laugh

laugh = make_laugh_func()
print(laugh())


# Outro Exemplo


def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHA', 'LOL', 'HEHEHE', 'AHUSHAUSHUAS'))
        return f'{laugh} {person}'
    return get_laugh

laugh_at = make_laugh_at_func('Linda')
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())





