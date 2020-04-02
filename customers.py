from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('product.html')

@app.route('/orders', methods=['POST'])
def write_order():
    email_receive = request.form['email_give']
    number_receive = request.form['number_give']
    count_receive = request.form['count_give']

    order = {
        'email' : email_receive,
        'number' : number_receive,
        'count' : count_receive
    }

    db.orders.insert_one(order)
    return jsonify({'result':'success', 'msg':'주문이 완료되었습니다.'})

@app.route('/orders', methods=['GET'])
def read_order():
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result':'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0',port=8000,debug=False)