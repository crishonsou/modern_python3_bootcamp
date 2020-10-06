# Decorators são funções
# São exemplos de Higher Order Functions
# Usam a sintaxe @
# Herdam o comportamento de funções

# Decorators como Funções

def be_polite(fn):
    def wrapper():
        print('What a pleasure to meet you')
        fn()
        print('Have a great day')
    return wrapper

def greet():
    print('My name is Colt')

def rage():
    print('I hate you')


greet = be_polite(greet)
polite_rage = be_polite(rage)
greet()
polite_rage()


# Decorator como Suggar Syntax

def be_polite(fn):
    def wrapper():
        print('What a pleasure to meet you')
        fn()
        print('Have a great day')
    return wrapper

@be_polite
def greet():
    print('My name is Colt')
    
@be_polite
def rage():
    print('I hate you')

greet()
rage()





