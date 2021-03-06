from flask import Flask, jsonify

app = Flask(__name__)

stores = [
{
'name':'my awesome store',
'items':[
        {
        'name': 'weirdthing',
        'price': '17.99'
         }
        ]
    }
]

# POST /store data: (name:)
@app.route('/store', methods = ['POST'])
def create_store():
        pass

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST /store data: (name:)
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
        pass 

app.run(port=5000)