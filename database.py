import sqlite3 as sq 

conn = sq.connect("passwords.db")
cur = conn.cursor()

cur.execute("CREATE TABLE mainpassword ( mpword TEXT )") # To save the main passowrd 
cur.execute("INSERT INTO mainpassword VALUES('')") # create empty main password 

cur.execute("CREATE TABLE passwords ( title TEXT , pword TEXT )") # To save passwords 

conn.commit()
conn.close()