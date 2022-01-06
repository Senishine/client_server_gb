""" Реализовать простое клиент - серверное взаимодействие по протоколу JIM (JSON instant messaging):
клиент отправляет запрос серверу;
сервер отвечает соответствующим кодом результата.
Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
Функции клиента:
сформировать presence-сообщение;
отправить сообщение серверу;
получить ответ сервера;
разобрать сообщение сервера;
параметры командной строки скрипта client.py <addr> [<port>]:
addr — ip-адрес сервера;
port — tcp-порт на сервере, по умолчанию 7777.
"""

from argparse import ArgumentParser
from socket import socket, AF_INET, SOCK_STREAM
import time

from messages import MessageType, ServerResponseFieldName
from utils import send_message, get_data

from log.client_log_config import logger

def create_presence_msg(account_name, status=''):
    return {
        'action': MessageType.PRESENCE.value,
        'time': time.time(),
        'type': 'status',
        'user': {
            'account_name': account_name,
            'status': status
        }
    }


def create_client_socket(address, port):
    logger.info('Creating new socket [address=%s, port=%s]', address, port)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address, port))
    return s


def handle_response(message):
    logger.info('Received response from server [message=%s]', message)
    assert message is not None, 'Message is None'
    code = message.get(ServerResponseFieldName.RESPONSE.value)
    assert code is not None, f'No {ServerResponseFieldName.RESPONSE.value} field in message'

    if code == 200:
        logger.info('Received successful response from server [message=%s]', message)
        return True
    else:
        logger.info('Received invalid response from server [message=%s]', message)
        return False


def test(data, address, port):
    logger.info(f'***** STARTING TEST *****')
    client_socket = create_client_socket(address, port)
    logger.info(f'sending data to server %s', data)
    send_message(data, client_socket)
    server_json = get_data(client_socket)
    logger.info(f'received response from server %s', server_json)
    try:
        handle_response(server_json)
    except AssertionError as e:
        logger.error('Error occurred during server response handling [address=%s, port=%s, error=%s]', address, port, e)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-a", "--address", help="address of remote server", default='localhost')
    parser.add_argument("-p", "--port", help="port of remote server", default=7777)

    args = parser.parse_args()

    test(create_presence_msg('Oksana'), args.address, args.port)
    test({
        'action': 'invalid_action',
        'time': time.time(),
        'type': 'status',
        'user': {
            'account_name': 'Oksana',
            'status': 'status'
        }
    }, args.address, args.port)
