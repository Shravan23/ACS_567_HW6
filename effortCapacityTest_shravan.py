import unittest
from effort_capacity_calculator import EffortCapacityCalculator

class TestEffortCapacityCalculator(unittest.TestCase):
    """
    Test cases for the calculate_team_effort_hours method of the EffortCapacityCalculator class.
    """

    def test_calculate_team_effort_hours_empty_team(self):
        """
        Test that the method returns 0 for average hours and total hours when the team members details are empty.
        """
        avg_hours, total_hours = EffortCapacityCalculator.calculate_team_effort_hours(10, [], 8)
        self.assertEqual(avg_hours, 0)
        self.assertEqual(total_hours, 0)

    def test_calculate_team_effort_hours_valid_input(self):
        """
        Test that the method correctly calculates average and total effort hours with valid team members details.
        """
        team_members_details = [
            {'pto_days': 2, 'ceremony_days': 1},
            {'pto_days': 1, 'ceremony_days': 2}
        ]
        avg_hours, total_hours = EffortCapacityCalculator.calculate_team_effort_hours(10, team_members_details, 8)
        self.assertEqual(avg_hours, 56)
        self.assertEqual(total_hours, 112)

    def test_calculate_team_effort_hours_all_pto_and_ceremony_days(self):
        """
        Test that the method handles cases where PTO and ceremony days equal or exceed the sprint days.
        """
        team_members_details = [
            {'pto_days': 10, 'ceremony_days': 0},
            {'pto_days': 5, 'ceremony_days': 5}
        ]
        avg_hours, total_hours = EffortCapacityCalculator.calculate_team_effort_hours(10, team_members_details, 8)
        self.assertEqual(avg_hours, 0)
        self.assertEqual(total_hours, 0)

if __name__ == '__main__':
    unittest.main()
