import unittest
from unittest.mock import patch
from main_gui import SprintCalculatorApp
import tkinter as tk
import time 

class TestSprintCalculatorApp(unittest.TestCase):
    """
    Acceptance tests for the SprintCalculatorApp, specifically testing the calculation of sprint team's velocity.
    """

    def setUp(self):
        """
        Set up the test environment by initializing the app with a hidden main window.
        """
        self.root = tk.Tk()
        self.app = SprintCalculatorApp(self.root)
        self.root.withdraw()  # Hide the main window during tests

    @patch('tkinter.simpledialog.askstring')
    @patch('tkinter.messagebox.showinfo')
    def test_calculate_velocity_happy_path(self, mock_showinfo, mock_askstring):
        """
        Test the happy path for calculating sprint team's velocity.
        
        Steps:
        1. Simulate user input for sprint points ("10,20,30,40").
        2. Trigger the calculate_velocity method.
        3. Verify that the correct average velocity (25.00) is displayed to the user.
        """
        # Simulate user input for sprint points and expected average velocity calculation
        mock_askstring.return_value = '10,20,30,40'
        
        # Trigger the calculate_velocity method which is bound to the "Calculate Velocity" button
        self.app.calculate_velocity()
        
        # Check if the correct message is displayed to the user
        self.assertEqual(self.app.result_label.cget("text"), "Average Velocity: 25.00")

    @patch('tkinter.simpledialog.askinteger')
    @patch('tkinter.simpledialog.askstring')
    def test_calculate_effort_capacity_happy_path(self, mock_askstring, mock_askinteger):
        """
        Test the happy path for calculating team effort-hour capacity.
        
        Steps:
        1. Manually set necessary attributes.
        2. Trigger the calculate_effort_capacity method.
        3. Verify that the correct average and total effort-hours are displayed.
        """
        # Manually set necessary attributes
        self.app.sprint_days = 10
        self.app.hours_per_day = 8
        self.app.team_members_details = [{'pto_days': 2, 'ceremony_days': 1}, {'pto_days': 1, 'ceremony_days': 2}]
        
        print("Attributes set:")
        print(f"sprint_days: {self.app.sprint_days}, hours_per_day: {self.app.hours_per_day}, team_members_details: {self.app.team_members_details}")
        time.sleep(2)  # Optional: Delay to observe the output
    
        # Now call the method under test
        self.app.calculate_effort_capacity()
        
        # Check if the correct message is displayed in the result label
        expected_text = "Average Effort-Hours/Person: 56.00, Total Effort-Hours for Team: 112.00"
        self.assertEqual(self.app.result_label.cget("text"), expected_text)

if __name__ == '__main__':
    unittest.main()