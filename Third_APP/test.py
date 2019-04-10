import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username string, password text)"

cursor.execute(create_table)

user = [
    (1, "Junchen", "wasd"),
    (2, "Jose", "lkjh"),
    (3, "Yaya", "qwer")
]

insert_query = "INSERT INTO users VALUES (?,?,?)"
select_query = "SELECT * FROM users"

cursor.executemany(insert_query, user)
for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()
