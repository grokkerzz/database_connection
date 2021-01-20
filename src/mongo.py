import pymongo
import logging

logger = logging.getLogger(__name__)

class MongoConnection:
    def __init__(self, *args, **kwargs):
        self.url = kwargs.get('url')
        self.username = kwargs.get('username', 'root')
        self.password = kwargs.get('password', '')
        self.host = kwargs.get('host', 'localhost')
        self.port = kwargs.get('port', 27017)

    def __enter__(self):
        if not self.url:
            self.client = pymongo.MongoClient(
                host=self.host,
                port=self.port
            )
            logger.info(f'Mongo: Create connection to {self.document}')
        else:
            self.client = pymongo.MongoClient(
                connect=self.url
            )
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
