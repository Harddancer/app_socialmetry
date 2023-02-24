import pika
import random
import time
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='anketa')


def callback(ch, method, properties, body):
    """
    Обработка чтения из очереди
    """
    name = body
    # Начинаем фыормирование анкеты
    formatanketa_time = random.randint(3, 40)
    time.sleep(formatanketa_time)
    # После окончания отправляем запрос
    requests.post('http://127.0.0.1:5000/format/',
                  data={'name': name, 'age': 100})


channel.basic_consume(queue='anketa', on_message_callback=callback)

print('start')
channel.start_consuming()
