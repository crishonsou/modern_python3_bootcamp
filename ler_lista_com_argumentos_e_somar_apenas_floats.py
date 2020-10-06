def sum_floats(*args):
    sumItens = []
    for j in args:
        if type(j) == float:
            sumItens.append(j)
            j += 1
    return sum(sumItens)
    return 0

#def sum_floats(*args):
#    return sum(arg for arg in args if type(arg) == float)        


print(sum_floats(1.5, 2.4, 'awesome', [], 1))
print(sum_floats(1,2,3,4,5))
