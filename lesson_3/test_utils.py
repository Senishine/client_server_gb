import unittest
from server import send_message, get_data
import mock
from utils import DEFAULT_ENCODING
import json


class TestSendMessage(unittest.TestCase):
    def test_send_none_message(self):
        # Given
        sock = mock.Mock()
        message = None

        # When # Then
        self.assertRaises(ValueError, send_message, message, sock)
        sock.send.assert_not_called()

    def test_send_str_message(self):
        # Given
        sock = mock.Mock()
        message = '{"response": 200}'

        # When
        send_message(message, sock)

        # Then
        sock.send.assert_called_once_with(message.encode(DEFAULT_ENCODING))

    def test_send_number_message(self):
        # Given
        sock = mock.Mock()
        message = 150

        # When # Then
        self.assertRaises(ValueError, send_message, message, sock)
        sock.send.assert_not_called()

    def test_send_dict_message(self):
        # Given
        sock = mock.Mock()
        message = {"response": 200}
        expected = json.dumps(message).encode(DEFAULT_ENCODING)

        # When
        send_message(message, sock)

        # Then
        sock.send.assert_called_once_with(expected)

    def test_send_bytes_message(self):
        # Given
        sock = mock.Mock()
        message = '{"response": 200}'.encode(DEFAULT_ENCODING)

        # When
        send_message(message, sock)

        # Then
        sock.send.assert_called_once_with(message)


if __name__ == '__main__':
    unittest.main()
