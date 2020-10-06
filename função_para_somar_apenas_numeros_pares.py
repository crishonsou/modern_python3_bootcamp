def sum_even_values(*args):
    even = []
    for i in args:
        if i % 2 != 1:
            even.append(i)
            i += 1        
    return sum(even)
    return 0

#def sum_even_values(*args):
#    return sum(arg for arg in args if arg % 2 == 0)
    

print(sum_even_values(1, 2, 3, 4, 5, 6))
print(sum_even_values(4, 2, 1, 10))
print(sum_even_values(1))
