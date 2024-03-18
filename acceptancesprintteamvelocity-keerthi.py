import unittest
from unittest.mock import patch
from main_gui import SprintCalculatorApp
import tkinter as tk

class TestSprintCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = SprintCalculatorApp(self.root)
        self.root.withdraw()  # Hide the main window to avoid GUI popping up

    @patch('tkinter.simpledialog.askstring')
    def test_calculate_velocity_happy_path(self, mock_askstring):
        mock_askstring.return_value = '30,40,35'
        expected_velocity_text = "Average Velocity: 35.00"

        self.app.calculate_velocity()

        self.assertEqual(self.app.result_label.cget("text"), expected_velocity_text, "The result label should display the correct average velocity")

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
