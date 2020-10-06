class Animal():
    def speak(self):
        raise NotImplementedError('Subclass needs to implement this method')

class Dog(Animal):
    def speak(self):
        return 'woof'

class Cat(Animal):
    def speak(self):
        return 'meow'

class Fish(Animal):
    pass


bella = Animal()
print(bella.speak())

bella = Dog()
print(bella.speak())

bella = Cat()
print(bella.speak())

bella = Fish()
print(bella.speak())




