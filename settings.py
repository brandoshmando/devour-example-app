import os

DEVOUR_ROUTES = {
    "default":"src.consumers.DefaultConsumer"
}

DEVOUR_CONFIG = {
    'hosts': os.environ.get('KAFKA'),
    'zookeeper_hosts': os.environ.get('ZOOKEEPER')
}
