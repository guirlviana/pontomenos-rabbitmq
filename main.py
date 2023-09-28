import sys
import time
from random import randint
from datetime import datetime
import json
import uuid

from rabbitMQ.consumer import Consumer
from rabbitMQ.publisher import Publisher


def convert_message_received(ch, method, properties, body):
    print(ch, method, properties)
    time_expected = randint(0, 5)
    print('\033[93m I get the message!\033[00m')
    print(f"\033[93m Let's start digging, it might take a while! expected time: {time_expected}s\033[00m")
    time.sleep(time_expected)
    body_as_dict = json.loads(body)
    print('\033[97m=== Your clock in ========= \033[00m')
    for key, value in body_as_dict.items():
        print(f'\033[94m {key}: {value}\033[00m')
    print('===========================')

if __name__ == '__main__':
    arguments = sys.argv[1:]

    if arguments[0] == 'consume':
        consumer = Consumer(convert_message_received)
        consumer.start()

    if arguments[0] == 'publish':
        publisher = Publisher()
        for i in range(int(arguments[3])):
            message = {'time': datetime.now().strftime('%d/%m/%Y - %H:%M:%S'), 'description': arguments[1], 'device': arguments[2], 'hash': str(uuid.uuid4())}
            message_as_json = json.dumps(message)
            publisher.publish(message_as_json)


