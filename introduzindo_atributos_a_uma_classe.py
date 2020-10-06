class User:
    active_users = 0
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
        
    def full_name(self):
        return f'{self.first} {self.last}'
    def initials(self):
        return f'{self.first[0]}.{self.last[0]}'
    def likes(self, thing):
        return f'{self.first} likes {thing}'
    def is_senior(self):
        if self.age >= 65:
            return f'{self.first} is a Senior'
        else:
            return f'{self.first} is not a Senior'
    def birthday(self):
        self.age += 1
        return f'Happy {self.age}th Birthday, {self.first}'
    def logout(self):
        User.active_users -= 1
        return f'{self.first} {self.last} has logged out!'
        
        
print(f'There is/are {User.active_users} active user(s).')     
        

user1 = User('Joe', 'Smith', 65)
user2 = User('Lara', 'Croft', 40)


print(user1.full_name())
print(user1.initials())

print(user2.full_name())
print(user2.initials())

print(f'There is/are {User.active_users} active user(s).')     

print(user2.logout())

print(f'There is/are {User.active_users} active user(s).')     




