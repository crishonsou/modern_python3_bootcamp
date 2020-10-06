class Animal:
    def make_sound(self, sound):
        self.sound = sound
        print(f'This animal says {self.sound}')
    cool = True

class Cat(Animal):
    pass

gandalf = Cat()
gandalf.make_sound('meow')
print(gandalf.cool)

bella = Animal()
bella.make_sound('auff')
print(bella.cool)

print(isinstance(bella, Cat))
print(isinstance(bella, Animal))
print(isinstance(gandalf, Cat))
print(isinstance(bella, Animal))



