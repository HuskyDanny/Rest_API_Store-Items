from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'item not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "The '{}' store is already there".format(name)}, 400

        store = StoreModel(name)
        try :
            store.save_to_db()
        except:
            return {'message':'something wrong during saving to db'},500
        

        return {'message':'successful'}, 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()  
            except:
                return {'message':'thing goes wrong when delete'}
        return {'message':'deleted'}
class StoreList(Resource):
    def get(self):
        return {'message':[store.json() for store in StoreModel.query.all()]}
            