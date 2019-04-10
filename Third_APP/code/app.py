from flask import Flask
from flask_restful import Api
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from flask_jwt import JWT
from datetime import timedelta

app = Flask(__name__)
api = Api(app)
app.secret_key = 'Allen'
#JWT configuration
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)
#create new endpoint for authentication
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(debug=True)
