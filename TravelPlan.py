from Activity import *

class TravelPlan:
    def __init__(self, name):
        # Initialize a new travel plan with a given name
        self.name = name
        self.activities = []  # List to hold activities
        
    def add_activity(self, activity):
        """Adds an activity to the travel plan."""
        self.activities.append(activity)

    def get_total_cost(self):
        """Calculates and returns the total cost of all activities."""
        # Use a list comprehension to sum the cost of each activity
        total_cost = sum(activity.cost for activity in self.activities)
        return total_cost

    def display_timeline(self):
        """Displays all activities in chronological order."""
        # Sort activities based on their date_time attribute
        sorted_activities = sorted(self.activities, key=lambda x: x.date_time)
        # Display details of each activity in the sorted order
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
    # Create sample activities
    activity1 = Activity("Beach Trip", "Visit the beach for a day", 100, "2024-10-30 10:00")
    activity2 = Activity("Mountain Hike", "Hiking in the mountains", 150, "2024-11-01 08:00")

    # Create a new travel plan
    name = "New travel plan"
    travel_plan = TravelPlan(name)  # Fixed: Pass 'name' to TravelPlan constructor
    
    # Add activities to the travel plan
    travel_plan.add_activity(activity1)
    travel_plan.add_activity(activity2)

    # Display total cost of the travel plan
    print(f"Total Cost: ${travel_plan.get_total_cost()}")
    
    # Display the timeline of activities
    travel_plan.display_timeline()
    
    # Delete an activity and display the updated timeline
    travel_plan.delete_activity("Beach Trip")
    travel_plan.display_timeline()
