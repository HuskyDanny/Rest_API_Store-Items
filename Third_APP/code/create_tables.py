import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,"+\
                "username text, password text)"
insert_data = "INSERT INTO users VALUES (NULL, ?, ?)"
cursor.execute(create_table)
cursor.execute(insert_data, ("Junchen", "wasd"))

create_table2 = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,"+\
                "name text, price real)"
insert_data2 = "INSERT INTO items VALUES (NULL, ?,?)"
cursor.execute(create_table2)
cursor.execute(insert_data2, ('Bear', 4.99))
connection.commit()

connection.close()
