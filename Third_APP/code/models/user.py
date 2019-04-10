import sqlite3
class UserModel:

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "Select * From users where username=?"
        result = cursor.execute(select_query, (username,))
        row = result.fetchone()

        if row:
            user = cls(*row )
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id_):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "Select * From users where id=?"
        result = cursor.execute(select_query, (id_,))
        row = result.fetchone()

        if row:
            user = cls(*row )
        else:
            user = None

        connection.close()
        return user
