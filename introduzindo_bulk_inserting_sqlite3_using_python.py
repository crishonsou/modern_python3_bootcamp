import sqlite3

# create/open the connection

conn = sqlite3.connect("c:\sqlite\my_friends.db")

# create cursor object

cursor = conn.cursor()

# execute sql commands

people = [
    ("Emerson", "Andrade", 30),
    ("Antonio", "Ventura", 30),
    ("Marcelo", "Endo", 12),
    ("Bruno", "Manente", 12),
    ("Daniel", "Fly", 12),
    ("Guilherme", "Cascapera", 12)]

# Good way
for person in people:
    cursor.executemany(f"INSERT INTO friends (first_name, last_name, closeness) VALUES (?, ?, ?)", person
)
    print("INSERTING!!") 


# Better way
cursor.executemany(f"INSERT INTO friends (first_name, last_name, closeness) VALUES (?, ?, ?)", people
)

# commit changes
conn.commit()


# close connection
conn.close()


