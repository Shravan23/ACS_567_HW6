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
        time.sleep(2)
        
        # Check if the correct message is displayed to the user
        self.assertEqual(self.app.result_label.cget("text"), "Average Velocity: 25.00")

if __name__ == '__main__':
    unittest.main()