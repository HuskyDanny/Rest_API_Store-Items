#API class, have specifc endpoint defined in app.py

import sqlite3
from flask_jwt import jwt_required
from flask_restful import Resource, reqparse
from models.item import ItemModel
from flask import jsonify
class Item(Resource):
    #Enforce the arguments, parse_args will return those values
    #price here is required
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type = float,
        required = True,
        help = "Errors with Price Filed"
    )

    #@jwt is used to enforce authentication
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'name did not match'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':'name already exists'}, 400
        #getting the data from body, only get price here because reqparse
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.save_to_db()
        except:
            return {"message":"Error occurred when inserting"}, 500

        return item.json(), 201

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        
        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, data['price'])

        item.save_to_db()
        return {"message":"Update completed"}

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        try:
            item.delete_from_db()
        except:
            return {"message":"Delete Failed"},500
        return {'message':'item deleted'}

class ItemList(Resource):

    def get(self):
        return {'items' : [model.json() for model in ItemModel.query.all()]}    
