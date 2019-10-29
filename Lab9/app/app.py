
#!flask/bin/python
from flask import Flask, jsonify, redirect, render_template
from pymongo import MongoClient

import datetime

app = Flask(__name__)
client = MongoClient('mongodb://db1:27017,db22:27018,db33:27019/?replicaSet=rs0')  
db = client.mymongodb  
tasks_collection = db.task  
initial_tasks = [task for task in tasks_collection.find()]

if (len(initial_tasks)) == 0:
    tasks_collection.insert({
        'timestamp': datetime.datetime.utcnow(),
        'user': 'User1',
        'message': 'Buy groceries'
    })
    tasks_collection.insert({
        'timestamp': datetime.datetime.utcnow(),
        'user': 'User2',
        'message': 'Learn Python'
    })


@app.route('/', methods=['GET'])
def get_tasks():
    all_messages = tasks_collection.find()
    return render_template('index.html', messages=all_messages)


@app.route('/<string:name>/<string:message>', methods=['GET'])
def create_task(name, message):
    new_message = {"timestamp":datetime.datetime.utcnow(), "user":name,"message": message}
    tasks_collection.insert(new_message)
    return redirect('/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



