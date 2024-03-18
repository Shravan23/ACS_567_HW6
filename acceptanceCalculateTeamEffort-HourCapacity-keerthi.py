
import tkinter as tk
from tkinter import simpledialog
from main_gui import SprintCalculatorApp

class AcceptanceTestCalculateTeamEffortHourCapacity:
    def run_test(self):
        # Setup the application
        root = tk.Tk()
        app = SprintCalculatorApp(root)
        root.withdraw()  # Hide the main window to avoid GUI popping up during the test

        # Mock user inputs for sprint days, hours per day, and team member details
        # This part depends on how your application accepts inputs. You might need to directly
        # set variables or use a mocking framework to simulate dialog responses.
        app.sprint_days = 10
        app.hours_per_day = 8
        app.team_members_details = [
            {'pto_days': 2, 'ceremony_days': 1},
            {'pto_days': 1, 'ceremony_days': 2}
        ]

        # Trigger the calculation
        app.calculate_effort_capacity()

        # Check the result against expectations
        expected_result = "Average Effort-Hours/Person: 56.00, Total Effort-Hours for Team: 112.00"
        actual_result = app.result_label.cget("text")
        assert actual_result == expected_result, f"Expected '{expected_result}', got '{actual_result}'"

        print("Acceptance Test Passed: Correct effort-hour capacity calculated.")

if __name__ == "__main__":
    test = AcceptanceTestCalculateTeamEffortHourCapacity()
    test.run_test()
