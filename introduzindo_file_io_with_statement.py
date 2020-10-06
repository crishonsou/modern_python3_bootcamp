#file = open("text.txt")
#file.read()
#file.close()

with open("text.txt") as file:
    data = file.read()

print(data)
