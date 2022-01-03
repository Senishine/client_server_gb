import unittest
import time
from client import create_presence_msg, create_client_socket, handle_response
from messages import ServerResponseFieldName, MessageType
import mock


class TestCreatePresenceMsg(unittest.TestCase):

    @mock.patch('time.time')
    def test_create_presence_msg(self, mocked_time):
        # Given
        test_value = 42
        account = 'Mika'
        mocked_time.return_value = test_value
        expected = {
            'action': MessageType.PRESENCE.value,
            'time': test_value,
            'type': 'status',
            'user': {
                'account_name': account,
                'status': ''
            }
        }

        # When
        response = create_presence_msg(account)

        # Then
        self.assertEqual(expected, response)


class TestHandleResponse(unittest.TestCase):
    def test_handle_response(self):
        # Given
        test_data = {
            'response': 200
        }

        # When
        result = handle_response(test_data)

        # Then
        self.assertTrue(result, 'expected True')

    def test_handle_response_with_absent_message(self):
        # Given
        message = None

        # When # Then
        self.assertRaises(AssertionError, handle_response, message)

    def test_handle_response_with_empty_message(self):
        # Given
        message = {}

        # When # Then
        self.assertRaises(AssertionError, handle_response, message)


if __name__ == "__main__":
    unittest.main()
