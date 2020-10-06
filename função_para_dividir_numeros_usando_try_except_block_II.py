def divide(num1, num2):
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return 'Please do not divide by 0'
    except TypeError:
        return 'Please provide two integers or floats!'
    else:
        return(f'{num1} divided by {num2} is {result:.0f}')


print(divide(4, 2))
print(divide([], '1'))
print(divide(1, 0))
