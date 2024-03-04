# main_gui.py

import tkinter as tk
from tkinter import simpledialog, messagebox
from velocity_calculator import VelocityCalculator

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



if __name__ == "__main__":
    root = tk.Tk()
    app = SprintCalculatorApp(root)
    root.mainloop()
