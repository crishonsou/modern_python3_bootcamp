# _name - Forma convencional de indicar uma váriavel ou método ou propriedade privada
# __name - Mangling Name. Só poderemos acessá-la se incluirmos a Classe
# __name__ - Dunder method - especifico para Python

class Person:
    def __init__(self):
        self.name = 'Cristiano'
        self._secret = 'hi'
        self.__msg = 'I like turtles'
        self.__lol = 'HAHAHAHAHAHA'
            

p = Person()

print(p.name)
print(p._secret)
print(dir(p))
print(p._Person__msg)
print(p._Person__lol)

        
