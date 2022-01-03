import unittest
from server import send_message, get_data
import mock


class TestSendMessage(unittest.TestCase):
    def test_send_message(self):
        # Given
        sock = mock.Mock()
        message = None

        # When # Then
        self.assertRaises(AssertionError, send_message, message, sock)
        sock.send.assert_not_called()


if __name__ == '__main__':
    unittest.main()
