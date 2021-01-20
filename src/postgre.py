import psycopy2
import logging

class PostgreConnection:
	def __inti__(self, *args, **kwargs):
		self.username = kwargs['username']
		self.password = kwargs['password']
		self.schema = kwargs.get('schema', 'public')
		self.database = kwargs['database']
		self.host = kwargs.get('host', '127.0.0.1')
		self.port = kwargs.get('port', 5432)
	
	def __enter__(self):
		self.connection = psycopy2.connect(
			dbname=self.database,
			username = self.username,
			password = self.password,
			host=self.host,
			port=self.port
		)
		logging.info(f'Postgresql: Create connection to {self.schema}.{self.database}')
		return self.connection

	def __exit__(self, exc_type, exc_val, exc_tb):
		logging.info(f'Postgresql: Close connection to {self.schema}.{self.database}')
		self.connection.close()
