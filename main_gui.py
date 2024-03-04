# main_gui.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from velocity_calculator import VelocityCalculator
from effort_capacity_calculator import EffortCapacityCalculator

class SprintCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Sprint Calculator")

        # Buttons
        tk.Button(master, text="Calculate Velocity", command=self.calculate_velocity).pack(pady=5)
        tk.Button(master, text="Calculate Effort Capacity", command=self.prompt_effort_capacity_details).pack(pady=5)
        
        # Result label
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def calculate_velocity(self):
        sprint_points_str = simpledialog.askstring("Input", "Enter sprint points separated by commas (e.g., 30,40,35):")
        try:
            sprint_points = list(map(int, sprint_points_str.split(',')))
            average_velocity = VelocityCalculator.calculate_average_velocity(sprint_points)
            self.result_label.config(text=f"Average Velocity: {average_velocity:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid list of sprint points.")

    def prompt_effort_capacity_details(self):
        self.team_members_details = []
        self.sprint_days = simpledialog.askinteger("Input", "Enter number of sprint days:")
        self.hours_per_day = simpledialog.askinteger("Input", "Enter number of working hours per day:")
        team_members = simpledialog.askinteger("Input", "Enter number of team members:")
        
        for i in range(team_members):
            pto_days = simpledialog.askinteger("Input", f"Enter PTO days for team member {i+1}:")
            ceremony_days = simpledialog.askinteger("Input", f"Enter ceremony days for team member {i+1}:")
            self.team_members_details.append({'pto_days': pto_days, 'ceremony_days': ceremony_days})
        
        self.calculate_effort_capacity()

    def calculate_effort_capacity(self):
        avg_hours, total_hours = EffortCapacityCalculator.calculate_team_effort_hours(
            self.sprint_days, self.team_members_details, self.hours_per_day
        )
        self.result_label.config(text=f"Average Effort-Hours/Person: {avg_hours:.2f}, Total Effort-Hours for Team: {total_hours:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SprintCalculatorApp(root)
    root.mainloop()
