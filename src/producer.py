import os
from pykafka import KafkaClient
import json

kafka_hosts = os.environ['KAFKA']
zk_hosts = os.environ['ZOOKEEPER']

client = KafkaClient(kafka_hosts, zk_hosts)

topic = client.topics['test']
producer = topic.get_sync_producer()
with topic.get_producer() as producer:
    while True:
        message = raw_input('Enter a message:')
        try:
            json.loads(message)
            producer.produce(message)
        except:
            print "Input must be json serializable"
