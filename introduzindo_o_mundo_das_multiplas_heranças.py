class Aquatic:
    def __init__(self, name):
        print('AQUATIC INIT!')
        self.name = name

    def swin(self):
        return f'{self.name} is swimming'

    def greet(self):
        return f'I am {self.name} out of the sea!'


class Ambulatory:
    def __init__(self, name):
        print('AMBULATORY INIT!')
        self.name = name

    def walk(self):
        return f'{self.name} is walking'

    def greet(self):
        return f'I am {self.name} of the land!'


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print('PENGUIN INIT!')
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)



#s1 = Aquatic('John')
#s2 = Ambulatory('Cesar')
s3 = Penguin('Capitain Hook')

#print(s1.swin())
#print(s1.greet())

#print(s2.walk())
#print(s2.greet())

#print(s3.swin())
#print(s3.greet())

print(s3)

print(f's3 is instance of Penguin: {isinstance(s3, Penguin)}')
print(f's3 is instance of Aquatic: {isinstance(s3, Aquatic)}')
print(f's3 is instance of Ambulatory: {isinstance(s3, Ambulatory)}')


