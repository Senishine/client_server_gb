from min_value import smallest_find
import unittest


class TestSmallestFind(unittest.TestCase):
    def test_smallest_find(self):
        # Given
        expected1 = 5
        expected2 = -160

        # When
        response1 = smallest_find([15, 10, 7, 1050, 5])
        response2 = smallest_find([0, 10, 7, 999, -5, -160])

        # Then
        self.assertEqual(expected1, response1)
        self.assertEqual(expected2, response2)

    def test_smallest_find_with_wrong_data_type(self):
        # Given
        test_data = {15: 10, 'key2': 1050}
        test_data_2 = '(0, 10, 7, 999, -5, -160)'

        # When  # Then
        self.assertRaises(AssertionError, smallest_find, test_data)
        self.assertRaises(AssertionError, smallest_find, test_data_2)


if __name__ == '__main__':
    unittest.main()
