#def my_for(iterable):
#    iterator = iter(iterable)
#    while True:
#        try:
#            print(next(iterator))
#        except StopIteration:
#            print('End of Iteration')
#            break

#my_for('Cristiano')
#my_for([1,2,3,4,5,6,7,8,9,10])        


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)

def sum(x):
    print(x + x)

def square(x):
    print(x * x)


my_for('lol', print)
my_for([1,2,3,4], sum)
my_for([1,2,3,4,5], square)




