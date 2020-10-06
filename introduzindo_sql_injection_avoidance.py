import sqlite3

conn = sqlite3.connect(r"c:\sqlite\users.db")

username = input('Please enter you username: ')
password = input('Please enter your password: ')

cursor = conn.cursor()

# Bad Idea
#query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

# Good Practice
query = f"SELECT * FROM users WHERE username = ? AND password = ?"

# Bad Idea
# cursor.execute(query)

# Good Practice
cursor.execute(query, (username, password))

result = cursor.fetchone()
if(result):
    print('Welcome Back')
else:
    print('Failed Login')

conn.commit()
conn.close()
