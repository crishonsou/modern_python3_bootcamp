#from csv import reader

#with open("fighters.csv") as f:
#    csv_reader = reader(f) # This is a iterator
#    next(csv_reader) # If you don´t need the readers
#    for fighter in csv_reader:
#        print(f'{fighter[0]} is from {fighter[1]}')
#        #each row in a list
#        #print(row)


#with open("fighters.csv") as f:
#    csv_reader = reader(f) # this is a iterator
#    data = list(csv_reader) # If you need the readers, turning into list
#    print(data)

from csv import DictReader

with open("fighters.csv") as f:
    csv_reader = DictReader(f)
    for row in csv_reader:
        #each row in a ordered Dict
        print(row)
    
