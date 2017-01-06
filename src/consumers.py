from devour.consumers import DevourConsumer
from .configurations import config_one

class DefaultConsumer(DevourConsumer):
    consumer_type = 'simple_consumer'
    consumer_topic = 'test'
    consumer_config = config_one

    def digest(self, x, y):
        print x+y
