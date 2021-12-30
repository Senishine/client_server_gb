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

from socket import socket, AF_INET, SOCK_STREAM
import time

from lesson_3.messages import MessageType, ServerResponseFieldName
from utils import send_message, get_data


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


def create_client_socket(address='localhost', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address, port))
    return s


def handle_response(message):
    code = message[ServerResponseFieldName.RESPONSE.value]
    if code == 200:
        print(f'Received successful response from server {message}')
    else:
        print(f'Received invalid response from server {message}')


def test(data):
    print()
    print(f'***** STARTING TEST *****')
    client_socket = create_client_socket()
    print(f'sending data to server {data}')
    send_message(data, client_socket)
    server_json = get_data(client_socket)
    print(f'received response from server {server_json}')
    handle_response(server_json)


if __name__ == '__main__':
    test(create_presence_msg('Oksana'))
    test({
        'action': 'invalid_action',
        'time': time.time(),
        'type': 'status',
        'user': {
            'account_name': 'Oksana',
            'status': 'status'
        }
    })
