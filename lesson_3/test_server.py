import time
import unittest

import mock

from messages import MessageType
from server import create_response, accept_client_connection, handle_request


class TestCreateResponse(unittest.TestCase):
    def test_create_response_without_message(self):
        # Given
        expected1 = {'response': 400}
        expected2 = {'response': 201}

        # When
        response1 = create_response(400)
        response2 = create_response(201)

        # Then
        self.assertEqual(expected1, response1)
        self.assertEqual(expected2, response2)

    def test_create_response_with_defaults(self):
        # Given
        expected = {'response': 200}

        # When
        response = create_response()

        # Then
        self.assertEqual(expected, response)

    def test_create_response_with_error_message(self):
        # Given
        msg = 'unauthorised'
        code = 401
        expected = {'response': code, 'error': msg}

        # When
        response = create_response(code, msg)

        # Then
        self.assertEqual(expected, response)

    def test_create_response_with_alert_message(self):
        # Given
        msg = 'redirect'
        code = 301
        expected = {'response': code, 'alert': msg}

        # When
        response = create_response(code, msg)

        # Then
        self.assertEqual(expected, response)

    @mock.patch('server.get_data')
    @mock.patch('server.send_message')
    @mock.patch('server.handle_request')
    def test_accept_client_connect(self, mocked_handle_request, mocked_send_message, mocked_get_data):
        # Given
        client_response = {'response': 200}
        client_socket = mock.Mock()
        client_data = {
            'action': MessageType.PRESENCE.value,
            'time': time.time(),
            'type': 'status',
            'user': {
                'account_name': 'test_user',
                'status': ''
            }
        }
        mocked_get_data.return_value = client_data

        # When
        accept_client_connection(client_socket)

        # Then
        mocked_handle_request.assert_called_once_with(client_data)
        mocked_send_message.assert_called_once_with(client_response, client_socket)
        client_socket.close.assert_called_once()

    @mock.patch('server.get_data')
    @mock.patch('server.send_message')
    @mock.patch('server.handle_request')
    def test_accept_client_connect_with_error(self, mocked_handle_request, mocked_send_message, mocked_get_data):
        # Given
        client_response = {'response': 400, 'error': 'Bad request'}
        client_socket = mock.Mock()
        mocked_get_data.side_effect = mock.Mock(side_effect=Exception('Test error'))

        # When
        accept_client_connection(client_socket)

        # Then
        mocked_handle_request.assert_not_called()
        mocked_send_message.assert_called_once_with(client_response, client_socket)
        client_socket.close.assert_called_once()

    @mock.patch('server.get_data')
    @mock.patch('server.send_message')
    @mock.patch('server.handle_request')
    def test_accept_client_connect_with_handle_request_error(self,
                                                             mocked_handle_request,
                                                             mocked_send_message,
                                                             mocked_get_data):
        # Given
        client_response = {'response': 400, 'error': 'Bad request'}
        client_socket = mock.Mock()
        client_data = {
            'action': MessageType.PRESENCE.value,
            'time': time.time(),
            'type': 'status',
            'user': {
                'account_name': 'test_user',
                'status': ''
            }
        }
        mocked_get_data.return_value = client_data
        mocked_handle_request.side_effect = mock.Mock(side_effect=Exception('Test error'))

        # When
        accept_client_connection(client_socket)

        # Then
        mocked_handle_request.assert_called_once()
        mocked_send_message.assert_called_once_with(client_response, client_socket)
        client_socket.close.assert_called_once()

    def test_handle_message(self):
        # Given
        test_data = {
            'action': MessageType.PRESENCE.value
        }

        # When
        result = handle_request(test_data)

        # Then
        self.assertIsNone(result)

    def test_handle_message_with_wrong_action(self):
        # Given
        test_data = {
            'action': 'invalid_action'
        }

        # When # Then
        self.assertRaises(ValueError, handle_request, test_data)

    def test_handle_message_with_absent_action(self):
        # Given
        test_data = {}

        # When # Then
        self.assertRaises(ValueError, handle_request, test_data)


if __name__ == "__main__":
    unittest.main()
