from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'Allen'
#create new endpoint /auth
jwt = JWT(app, authenticate, identity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "Errors with Price Filed"
    )

    @jwt_required()
    def get(self, name):
        #next is an iterator getting you the next item in the filter object
        item = next(filter(lambda x : x['name'] == name, items), None)
        #the number indicating request not successful
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "The item '{}' has already existed ".format(name)}, 400

        data = Item.parser.parse_args()
        item = {'name' : name, 'price' : data['price']}
        items.append(item)
        return item, 201

    def put(self, name):
        data = Item.parser.parse_args()

        item = next(filter(lambda x: x['name'] == name, items),None)
        if item:
            item.update(data)
        else:
            item = {'name' : name, 'price': data['price']}
            items.append(item)
        return item


    def delete(self, name):
        global items
        items = list(filter(lambda x : x['name'] != name, items))
        return {'message':'item deleted'}

class Itemlist(Resource):

    def get(self):
        return {'items': items}


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Itemlist, '/items')
app.run(debug=True)
