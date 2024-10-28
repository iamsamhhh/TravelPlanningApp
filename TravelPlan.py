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

    def add_activity_from_input(self):
        """Adds an activity based on user input."""
        name = input("Enter activity name: ")
        description = input("Enter activity description: ")
        while True:
            try:
                cost = float(input("Enter activity cost: $"))
                break
            except ValueError:
                print("Please enter a valid number for cost.")
        
        while True:
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            try:
                # Validate date format by attempting to create an Activity
                Activity(name, description, cost, date_time)
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD HH:MM")
        
        new_activity = Activity(name, description, cost, date_time)
        self.add_activity(new_activity)
        print(f"Activity '{name}' added successfully.")


# Example Usage
if __name__ == "__main__":
    # Create a new travel plan
    plan_name = input("Enter travel plan name: ")
    travel_plan = TravelPlan(plan_name)
    
    while True:
        print("\nTravel Plan Menu:")
        print("1. Add activity")
        print("2. Delete activity")
        print("3. Display timeline")
        print("4. Show total cost")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            travel_plan.add_activity_from_input()
        
        elif choice == "2":
            activity_name = input("Enter activity name to delete: ")
            travel_plan.delete_activity(activity_name)
        
        elif choice == "3":
            travel_plan.display_timeline()
        
        elif choice == "4":
            print(f"Total Cost: ${travel_plan.get_total_cost()}")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")
