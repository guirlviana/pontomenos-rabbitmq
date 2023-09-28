import pika

from constants import HOST, PORT, USERNAME, PASSWORD


class Publisher:
    def __init__(self):
        self.__host = HOST
        self.__port = PORT
        self.__username = USERNAME
        self.__password = PASSWORD
        self.__exchange = 'pontomenos_ex'
        self.__queue = 'pontomenos_qu'
        self.__channel = self.__create_chanell()

    def __create_chanell(self):
        connection_parameters = pika.ConnectionParameters(
            host=self.__host,
            port=self.__port,
            credentials=pika.PlainCredentials(
                username=self.__username,
                password=self.__password
            )
        )

        channel = pika.BlockingConnection(connection_parameters).channel()

        channel.queue_declare(self.__queue, durable=True)
        channel.exchange_declare(self.__exchange, 'direct', durable=True)
        channel.queue_bind(self.__queue, self.__exchange, routing_key=f'{self.__queue}_rk')

        return channel

    def publish(self, message):
        self.__channel.basic_publish(self.__exchange, routing_key=f'{self.__queue}_rk',
                                     body=message,
                                     properties=pika.BasicProperties(
                                         delivery_mode=2
                                     ))