# writer 
# dictwriter

#from csv import writer

#with open("cats.csv", "w") as f:
#    csv_writer = writer(f)
#    csv_writer.writerow(["Name", "Age"])
#    csv_writer.writerow(["Blue", "3"])
#    csv_writer.writerow(["Kitty", "1"])

from csv import reader, writer

with open('fighters.csv') as f:
    csv_reader = reader(f)
    with open('screaming_fighters.csv', "w") as f:
        csv_writer = writer(f)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])




    
    


