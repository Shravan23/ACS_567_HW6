class EffortCapacityCalculator:
    @staticmethod
    def calculate_individual_effort_hours(sprint_days, pto_days, ceremony_days, hours_per_day):
        # Ensure no negative values
        available_days = max(sprint_days - (pto_days + ceremony_days), 0)
        return available_days * hours_per_day

    @staticmethod
    def calculate_team_effort_hours(sprint_days, team_members_details, hours_per_day):
        total_hours = 0
        for member in team_members_details:
            total_hours += EffortCapacityCalculator.calculate_individual_effort_hours(
                sprint_days, member['pto_days'], member['ceremony_days'], hours_per_day
            )
        
        average_hours = total_hours / len(team_members_details) if team_members_details else 0
        return average_hours, total_hours
