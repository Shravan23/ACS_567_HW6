import unittest
from velocity_calculator import VelocityCalculator

class TestVelocityCalculator(unittest.TestCase):
    """
    Test cases for the calculate_average_velocity method of the VelocityCalculator class.
    """

    def test_calculate_average_velocity_empty_list(self):
        """
        Test that the method returns 0 when the input list is empty.
        """
        self.assertEqual(VelocityCalculator.calculate_average_velocity([]), 0)

    def test_calculate_average_velocity_single_point(self):
        """
        Test that the method correctly calculates the average velocity with a single sprint point.
        """
        self.assertEqual(VelocityCalculator.calculate_average_velocity([5]), 5)

    def test_calculate_average_velocity_multiple_points(self):
        """
        Test that the method correctly calculates the average velocity with multiple sprint points.
        """
        self.assertEqual(VelocityCalculator.calculate_average_velocity([10, 20, 30, 40]), 25)

    def test_calculate_average_velocity_negative_points(self):
        """
        Test that the method correctly calculates the average velocity with negative sprint points.
        """
        self.assertEqual(VelocityCalculator.calculate_average_velocity([-10, 20, -30, 40]), 5)

    def test_calculate_average_velocity_non_integer_values(self):
        """
        Test that the method raises a TypeError when the input list contains non-integer values.
        """
        with self.assertRaises(TypeError):
            VelocityCalculator.calculate_average_velocity([10, "20", 30.5, 40])

if __name__ == '__main__':
    unittest.main()
