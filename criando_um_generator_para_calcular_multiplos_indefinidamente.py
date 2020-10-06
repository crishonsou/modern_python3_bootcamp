def get_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num


evens = get_multiples(4)

for nums in evens:
    print(nums)





    
