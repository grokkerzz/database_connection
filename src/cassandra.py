import logging
from cassandra.cluster import Cluster

def CassandraConnection:
    def __init__(self, *args, **kwargs):
        self.hosts = list(kwargs.get('hosts'))
        self.port = kwargs.get('port', 7000)

    def __enter__(self):
        self.cluster = Cluster(
            self.hosts
        )   
        return self.cluster
