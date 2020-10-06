class User:
    def __init__(self, first, last, age):
#        print('New user has been made')
        self.first = first
        self.last = last
        self.age = age



user1 = User("Leticia", "Carvalho", 35)
user2 = User("Cristiano", "Gonçalves", 44)

print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)




