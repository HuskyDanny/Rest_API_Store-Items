from flask import Flask, jsonify, request, render_template



#different key-value pair havs comma ","
stores =[
    {
        'name': 'Nike',
        'item': [
            {
            'name': 'AJ',
            'price':15.23
            }
        ]
    }
]



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#Post /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
    #get_json() already convert json string to python dicts
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(stores)

#Get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'Store not Found'})

@app.route('/store')
def get_all_stores():
    return jsonify(stores)

#Post /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            store['item'].append({'name':request_data['name'], 'price':request_data['price']})
    return jsonify({'message':'Store not found'})

#Get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['item'])
    return jsonify({'message':'Item not Found'})


if __name__ == '__main__':
    app.run(port=5000)