import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

cursor.execute("CREATE TABLE users (name TEXT, surname TEXT);")
cursor.execute(f"INSERT INTO users values (?, ?)",
               ("daniiar", "m"))
connection.commit()
connection.close()
