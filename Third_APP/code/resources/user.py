import sqlite3
from flask_restful import reqparse, Resource
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type = str, required = True)
    parser.add_argument("password", type = str, required = True)

    def post(self):
        data = UserRegister.parser.parse_args()
        #make sure this is before connection, or we will never close the connection
        #if things go wrong
        if UserModel.find_by_username(data['username']):
            return {'message' : 'username has been taken'}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        register_query = "INSERT INTO users VALUES (NULL, ?, ?)"

        cursor.execute(register_query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {'message': "User Registered Successfully"}, 201
