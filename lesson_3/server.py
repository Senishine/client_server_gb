""" Функции сервера:
принимает сообщение клиента;
формирует ответ клиенту;
отправляет ответ клиенту;
имеет параметры командной строки:
-p <port> — TCP-порт для работы (по умолчанию использует 7777);
-a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""
from socket import socket, AF_INET, SOCK_STREAM

from messages import MessageType, ServerResponseFieldName
from utils import send_message, get_data

from log.server_log_config import logger


def create_response(code=200, msg=None):
    logger.info('Creating response for client [code=%s, msg=%s]', code, msg)
    assert isinstance(code, int), 'code is not an integer'
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


def accept_client_connection(client_socket):
    try:
        client_json = get_data(client_socket)
        logger.info('received data from client [data=%s]', client_json)
        handle_request(client_json)
        response = create_response()
    except Exception as e:
        logger.error('error occurred during client request handling [client_socket=%s, error=%s]', client_socket, e)
        response = create_response(400, 'Bad request')
    logger.info('Sending response to client [client_socket=%s, response=%s]', client_socket, response)
    send_message(response, client_socket)
    client_socket.close()


def start_server(address='', port=7777):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((address, port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        logger.info('accepted client connection [client_address=%s]', addr)
        accept_client_connection(client)


def handle_request(message):
    action = message.get('action')
    if action == MessageType.PRESENCE.value:
        return
    raise ValueError('Unsupported action')


if __name__ == '__main__':
    start_server()
