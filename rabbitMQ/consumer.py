import pika

from constants import HOST, PORT, USERNAME, PASSWORD


class Consumer:
    def __init__(self, callback):
        self.__host = HOST
        self.__port = PORT
        self.__username = USERNAME
        self.__password = PASSWORD
        self.__queue = 'pontomenos_qu'
        self.__callback = callback
        self.__channel = self.__create_channel()

    def __create_channel(self):
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

        channel.basic_consume(self.__queue, auto_ack=True, on_message_callback=self.__callback)

        return channel

    def start(self):
        print('Joined...')
        self.__channel.start_consuming()
