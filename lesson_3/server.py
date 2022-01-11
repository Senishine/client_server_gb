""" Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
from socket import socket, AF_INET, SOCK_STREAM

from lesson_3.messages import MessageType, ServerResponseFieldName
from utils import send_message, get_data


def create_response(code=200, msg=None):
    data = {
        ServerResponseFieldName.RESPONSE.value: code
    }

    if msg is None:
        return data

    if 400 <= code <= 600:
        data[ServerResponseFieldName.ERROR.value] = msg
    else:
        data[ServerResponseFieldName.ALERT.value] = msg

    return data


def create_server_socket(address='', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        print(f'accepted client connection {addr}')
        try:
            client_json = get_data(client)
            print(f'received data from client is {client_json}')
            handle_request(client_json)
            response = create_response()
        except Exception as e:
            print(f'error occurred during client request handling {e}')
            response = create_response(400, 'Bad request')
        send_message(response, client)
        client.close()


def handle_request(message):
    if message['action'] == MessageType.PRESENCE.value:
        return
    raise ValueError('Unsupported action')


if __name__ == '__main__':
    server = create_server_socket()
