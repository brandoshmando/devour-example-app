from devour.consumers import DevourConsumer

config = {
    'reset_offset_on_start': True,
    'auto_offset_reset': 0
}

class DefaultConsumer(DevourConsumer):
    consumer_type = 'simple_consumer'
    consumer_topic = 'test'

    def digest(self, x, y):
        print x+y
