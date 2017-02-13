import os
from pykafka import KafkaClient
import json
from devour.handlers import ClientHandler

handler = ClientHandler()
producer = handler.get_producer('test')

while True:
    message = raw_input('Enter a message:')
    try:
        message = json.loads(message)
        producer.produce(message)
    except:
        print "Input must be json serializable"
