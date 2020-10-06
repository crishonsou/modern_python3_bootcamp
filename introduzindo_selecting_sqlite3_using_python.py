import sqlite3

# create/open the connection

conn = sqlite3.connect("c:\sqlite\my_friends.db")

# create cursor object

cursor = conn.cursor()

# cursor.execute("SELECT * FROM friends")
#cursor.execute("SELECT * FROM friends WHERE first_name is 'Jaime'")
cursor.execute("SELECT * FROM friends WHERE closeness > 12 ORDER BY closeness")


# Iterate over cursor
#for result in cursor:
#    print(result)

# Fetch all results as list
print(cursor.fetchall())

# Fetch One result
#print(cursor.fetchone())

# commit changes
conn.commit()


# close connection
conn.close()
