import sqlite3

# create/open the connection

conn = sqlite3.connect("c:\sqlite\my_friends.db")

# create cursor object

cursor = conn.cursor()

# execute sql commands

# silly way to do it (go to sql)
#insert_query = '''INSERT INTO friends
#                    VALUES ('Jaime', 'Henrique', 25)'''

# Bad way to use python for it
#first_name = 'Luis'
#last_name = 'Turci'
#closeness = 20

#query = f"INSERT INTO friends (first_name, last_name, closeness) VALUES ('{first_name}', '{last_name}', '{closeness}')"

# Better way to use python for use

form_data = ("Alexandre", "Sagaz", 4)
query = f"INSERT INTO friends (first_name, last_name, closeness) VALUES (?, ?, ?)"


cursor.execute(query, form_data)

# commit changes
conn.commit()


# close connection
conn.close()

