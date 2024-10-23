from Activity import *

class TravelPlan:
    def __init__(self, name):
        self.name = name
        self.activities = []  # List to hold activitys
    
    '''Function to create an empty travel plan'''
    def __init__(self):
        pass

    def add_activity(self, activity):
        """Adds an activity to the travel plan."""
        self.activities.append(activity)

    def show_total_cost(self):
        """Calculates and returns the total cost of all activitys."""
        total_cost = sum(activity.cost for activity in self.activities)
        return total_cost

    def display_timeline(self):
        """Displays all activitys in chronological order."""
        sorted_activities = sorted(self.activities, key=lambda x: x.date_time)
        for activity in sorted_activities:
            print(activity.display_activity_details())

    def delete_activity(self, activity_name):
        """Deletes an activity by name."""
        for activity in self.activities:
            if activity.name == activity_name:
                self.activities.remove(activity)
                print(f"Activity '{activity_name}' deleted successfully.")
                return
        print(f"Event '{activity_name}' not found.")


# Example Usage
if __name__ == "__main__":
    activity1 = Activity("Beach Trip", "Visit the beach for a day", 100, "2024-10-30 10:00")
    activity2 = Activity("Mountain Hike", "Hiking in the mountains", 150, "2024-11-01 08:00")

    travel_plan = TravelPlan()
    travel_plan.add_activity(activity1)
    travel_plan.add_activity(activity2)

    print(f"Total Cost: ${travel_plan.show_total_cost()}")
    travel_plan.display_timeline()
    travel_plan.delete_activity("Beach Trip")
    travel_plan.display_timeline()
