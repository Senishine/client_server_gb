""" Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
import json
from socket import socket, AF_INET, SOCK_STREAM


def create_server_socket(address='', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        print(f'Получен запрос на соединение от {client} {addr}')
        client_data = client.recv(640)
        if client_data is None:
            return
        print(f'received data from client is {client_data.decode("utf-8")}')
        # message =


def check_client_message(message, client_address):
    pass


if __name__ == '__main__':
    create_server_socket()
