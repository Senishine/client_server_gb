from plate_stack import PlateStack
import unittest


class TestPlateStack(unittest.TestCase):

    def test_push(self):
        # Given
        silver_plate_stack = PlateStack(10)
        plates = ['plate_' + str(plate) for plate in range(1, 23)]

        # When
        for plate in plates:
            silver_plate_stack.push(plate)

        # Then
        self.assertEqual(3, silver_plate_stack.stack_count())
        self.assertEqual(22, silver_plate_stack.size())

    def test_none_push(self):
        # Given
        silver_plate_stack = PlateStack(10)

        # When # Then
        self.assertRaises(AssertionError, silver_plate_stack.push, None)

    def test_boundary_value_push(self):
        # Given
        silver_plate_stack = PlateStack(10)
        plates2 = ['plate_' + str(plate) for plate in range(1, 32)]

        # When
        for plate in plates2:
            silver_plate_stack.push(plate)
        expected1 = 4

        # Then
        self.assertEqual(expected1, silver_plate_stack.stack_count())
        self.assertEqual(31, silver_plate_stack.size())

    def test_push_pop(self):
        # Given
        returned_by_pop = []
        gold_plate_stack = PlateStack(7)
        plates = ['plate_' + str(plate) for plate in range(1, 42)]
        for plate in plates:
            gold_plate_stack.push(plate)

        # When
        for _ in plates:
            returned_by_pop.append(gold_plate_stack.pop())
        returned_by_pop.reverse()

        # Then
        self.assertEqual(0, gold_plate_stack.stack_count())
        self.assertEqual(0, gold_plate_stack.size())
        self.assertEqual(plates, returned_by_pop)

    def test_boundary_value_pop(self):
        # Given
        silver_plate_stack = PlateStack(10)
        plates = ['plate_' + str(plate) for plate in range(1, 32)]
        for plate in plates:
            silver_plate_stack.push(plate)

        # When
        silver_plate_stack.pop()
        expected1 = 3

        # Then
        self.assertEqual(expected1, silver_plate_stack.stack_count())
        self.assertEqual(30, silver_plate_stack.size())

    def test_empty_pop(self):
        # Given
        silver_plate_stack = PlateStack(10)

        # When Then
        self.assertIsNone(silver_plate_stack.pop())
        self.assertEqual(0, silver_plate_stack.stack_count())
        self.assertEqual(0, silver_plate_stack.size())


if __name__ == '__main__':
    unittest.main()
