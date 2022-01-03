import json

DEFAULT_ENCODING = 'utf-8'


def send_message(message, sock):
    assert message is not None, 'Message is None'
    data_to_send = message
    if isinstance(message, str):
        data_to_send = message.encode(DEFAULT_ENCODING)
    elif isinstance(message, dict):
        data_to_send = json.dumps(message).encode(DEFAULT_ENCODING)
    sock.send(data_to_send)


def get_data(sock):
    data = sock.recv(640)
    return json.loads(data.decode(DEFAULT_ENCODING))
