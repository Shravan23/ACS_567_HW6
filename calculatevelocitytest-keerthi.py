import unittest
from velocity_calculator import VelocityCalculator

class TestVelocityCalculator(unittest.TestCase):
    def test_calculate_average_velocity_with_valid_points(self):
        sprint_points = [30, 40, 35]
        expected_average_velocity = sum(sprint_points) / len(sprint_points)
        self.assertEqual(
            VelocityCalculator.calculate_average_velocity(sprint_points),
            expected_average_velocity,
            "Should correctly calculate average velocity with valid sprint points"
        )

    def test_calculate_average_velocity_with_empty_list(self):
        sprint_points = []
        with self.assertRaises(ZeroDivisionError):
            VelocityCalculator.calculate_average_velocity(sprint_points)

# Add more tests here if needed

if __name__ == '__main__':
    unittest.main()
