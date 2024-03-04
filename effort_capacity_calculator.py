class EffortCapacityCalculator:
    @staticmethod
    def calculate_individual_effort_hours(sprint_days, pto_days, ceremony_days, hours_per_day):
        # Ensure no negative values
        available_days = max(sprint_days - (pto_days + ceremony_days), 0)
        return available_days * hours_per_day

