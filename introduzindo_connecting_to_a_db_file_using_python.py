import sqlite3

# create/open the connection

conn = sqlite3.connect("c:\sqlite\my_friends.db")

# create cursor object

cursor = conn.cursor()

# execute sql commands

cursor.execute("CREATE TABLE friends (first_name TEXT, last_name TEXT, closeness INTEGER);")


# commit changes
conn.commit()


# close connection
conn.close()
