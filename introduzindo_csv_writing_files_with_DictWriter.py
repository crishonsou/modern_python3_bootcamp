from csv import writer, DictWriter

with open("cats.csv", "w") as f:
    headers  = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(f, fieldnames=headers)
    csv_writer.writeheader() # It will write the headers inside the file for us
    csv_writer.writerow({
        "Name": "Garfield",
        "Breed": "Orange Tabby",
        "Age": 10
    })


from csv import DictReader, DictWriter

def cm_to_inch(cm):
    return float(cm) * 0.393701

with open("fighters.csv") as f:
    csv_reader = DictReader(f)
    fighters = list(csv_reader)
with open("inches_fighters.csv", "w") as f:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(f, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_inch(f["Height (in cm)"])
        })
