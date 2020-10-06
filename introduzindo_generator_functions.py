def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


for x in count_up_to(10):
    print(x)


counter = count_up_to(10)

for x in counter:
    print(x)
