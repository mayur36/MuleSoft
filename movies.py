
import sqlite3
cnt = sqlite3.connect("bollywood")
cnt.execute('''CREATE TABLE movies(
name TEXT,
actor TEXT,
actress TEXT,
yearOfRelease INTEGER,);''')
cnt.execute('''INSERT INTO movies VALUES(
'3 idiots', 'Amir Khan', 'Kareena Kapur', 2009);''')
cnt.commit()
cnt.execute('SELECT * FROM movies')
cnt.execute('SELECT * FROM movies WHERE actress = 'Kareena Kapur'')
















