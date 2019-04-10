import sqlite3

class ItemModel:

    def __init__(self, name, price=None):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name, 'price':self.price}

    #talking to db to find the given name record
    #since the method is used before creating this object, so we use classmethod
    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query_get = 'SELECT * FROM items WHERE name=?'
        result = cursor.execute(query_get, (name,))
        row = result.fetchone()
        connection.close()
        if row:
            #*rows unpack each element of row into parameters
            return cls(* row)

    #Insert into db by the given item(name,price)
    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query_post = 'INSERT INTO items VALUES(?,?)'
        cursor.execute(query_post, (self.name, self.price))
        connection.commit()
        connection.close()

    #Update the item with given name to price
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query_post = 'UPDATE items SET price=? WHERE name=?'
        cursor.execute(query_post, (self.price, self.name))
        connection.commit()
        connection.close()

    #delete the record with given name
    def delete_item(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query_delete = 'DELETE FROM items WHERE name=?'
        cursor.execute(query_delete, (self.name,))
        connection.commit()
        connection.close()
