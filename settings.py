import os

CONSUMER_ROUTES = {
    "default":"src.consumers.DefaultConsumer"
}

KAFKA_CONFIG = {
    'client': {
        'hosts': os.environ.get('KAFKA'),
        'zookeeper_hosts': os.environ.get('ZOOKEEPER'),
    },
    'consumer_routes': {
        'default':'src.consumers.DefaultConsumer'
    }
}
