import unittest
from effort_capacity_calculator import EffortCapacityCalculator

class TestTeamEffortHourCapacityAcceptance(unittest.TestCase):
    def test_team_effort_hour_capacity_happy_path(self):
        # Setup
        sprint_days = 10
        hours_per_day = 8
        team_members_details = [
            {'pto_days': 2, 'ceremony_days': 1},
            {'pto_days': 1, 'ceremony_days': 2}
        ]
        
        # Test individual effort hour calculation
        individual_hours_member_1 = EffortCapacityCalculator.calculate_individual_effort_hours(
            sprint_days, team_members_details[0]['pto_days'], team_members_details[0]['ceremony_days'], hours_per_day)
        individual_hours_member_2 = EffortCapacityCalculator.calculate_individual_effort_hours(
            sprint_days, team_members_details[1]['pto_days'], team_members_details[1]['ceremony_days'], hours_per_day)
        
        self.assertEqual(individual_hours_member_1, 56, "Individual effort hours for member 1 should be correctly calculated")
        self.assertEqual(individual_hours_member_2, 56, "Individual effort hours for member 2 should be correctly calculated")
        
        # Test team effort hour calculation
        avg_hours, total_hours = EffortCapacityCalculator.calculate_team_effort_hours(
            sprint_days, team_members_details, hours_per_day)
        
        self.assertEqual(avg_hours, 56, "Average effort hours per person should be correctly calculated")
        self.assertEqual(total_hours, 112, "Total effort hours for team should be correctly calculated")

if __name__ == '__main__':
    unittest.main()
