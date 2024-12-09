from flask import Flask, jsonify, request
import json
import os, signal


app = Flask(__name__)

data = [ {'id' : 1, 'name' : 'Jason'}, {'id' : 2, 'name': 'Achilles'}]
id_counter = 3


@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/send_data', methods=['POST'])
def send_data():
    person = json.loads(request.data)
    if not person.is_valid():
        return jsonify({"error":"bad_data"})
    
    person["id"] = id_counter
    id_counter += 1
    data.append(person)

    return jsonify({"success" : ""})

@app.route('/ping_server', methods=['POST'])
def ping_server():
    print("server has been pinged")
    return jsonify({"message" : "You have pinged the server"})

def data_valid(data):
    for key in data.keys():
        if key != 'name':
            return False
    return True


def start_defence():
    print("hello world")
    app.run(port=8000)