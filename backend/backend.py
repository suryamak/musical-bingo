from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import time, random

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin()
def ping():
    return 'Backend is online'

@app.route('/generate-board', methods=['GET'])
@cross_origin()
def generate():
    random.seed(time.time())
    items = []
    with open('txt/cleaned_items.txt', 'r') as file:
        items_raw = file.read()
        items = items_raw.split('\n')
        random.shuffle(items)
        return jsonify([items[:5], items[5:10], items[10:15], items[15:20], items[20:25]])

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=True)
    except:
        print("Error running server")