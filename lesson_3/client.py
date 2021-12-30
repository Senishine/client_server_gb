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
import  json


def create_client_socket(address='localhost', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((address, port))
    return s


def send_message(data_for_server, sock):
    if data_for_server is None:
        return
    binary_data = data_for_server.encode('utf-8') if isinstance(data_for_server, str) else data_for_server
    sock.send(binary_data)


def get_response(sock):
    data = sock.recv(1024)
    return data.decode('utf-8')


def check_response(message):
    pass

if __name__ == '__main__':
    client_socket = create_client_socket()
    send_message('Hello, it is me', client_socket)
    print(get_response(client_socket))

