from flask import Flask, json, request
import sqlite3
import pika
import settings
from db. create_db import createAnketa

tanketa = createAnketa()
print(tanketa)

app = Flask(__name__)
connection = sqlite3.connect(settings.DB_NAME, check_same_thread=False)
cursor = connection.cursor()

@app.route('/addmember/', methods=['POST'])
def addnewUser():
    data = request.form
    id = data['id']
    name = data['name']
    lastname = data['lastname']
    age = data['age']
    statement = f'INSERT INTO {settings.TABLE_NAME}(id,name,lastname,age) values (?,?,?,?)'
    cursor.execute(statement, (id, name, lastname, age))
    response = app.response_class(
        response=json.dumps({'STATUS': 'OK'}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/')
def infouser():
    statement = f"SELECT * FROM {settings.TABLE_NAME}"
    cursor.execute(statement)
    result = cursor.fetchall()
    print(result)
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/rezult/', methods=['POST'])
def queanketa():
    data = request.form
    id = data['id']
    name = data['name']
    lastname = data['lastname']
    age = data['age']
    statement = f'INSERT INTO {settings.TABLE_NAME}(id,name,lastname,age) values (?,?,?,?)'
    cursor.execute(statement, (id, name, lastname, age))

    # Публикуем сообщение в очередь
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='anketa')
    channel.basic_publish(exchange='',
                          routing_key='anketa',
                          body=name)
    connection.close()

    response = app.response_class(
        response=json.dumps({'STATUS': 'OK'}),
        status=200,
        mimetype='application/json'
    )
    return response





if __name__ == '__main__':
    app.run(debug=True)
