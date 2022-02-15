import sqlite3

#connection
cnt = sqlite3.connect("demo.db")
print('Connection established Successfully')

#create table
# cnt.execute('''CREATE TABLE movies(
# name TEXT,
# actor TEXT,
# actress TEXT,
# yearOfRelease INTEGER)''')
# print("Table Created Successfully")


#insert record
cnt.execute('''INSERT INTO movies VALUES(
'3 Idiots', 'Aamir Khan', 'Karina Kapur', 2009);''')
cnt.commit()
print("Record Insert Successfully")

#fetch record
cursor=cnt.execute("SELECT * FROM movies")
print(cursor.fetchall())

#fetch record with filter
cursor=cnt.execute("SELECT * FROM movies WHERE actor = 'Aamir Khan'")
print(cursor.fetchall())
