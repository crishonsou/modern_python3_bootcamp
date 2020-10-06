def week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

days = week()

for day in days:
    print(day)
