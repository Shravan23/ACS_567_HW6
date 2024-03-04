 # velocity_calculator.py

class VelocityCalculator:
    @staticmethod
    def calculate_average_velocity(sprint_points):
        total_points = sum(sprint_points)
        average_velocity = total_points / len(sprint_points)
        return average_velocity
