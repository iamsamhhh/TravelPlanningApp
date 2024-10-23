class Activity:
    def __init__(self, name, description, cost, date_time):
        """Initialize the activity with the given details."""
        self.name = name
        self.description = description
        self.cost = cost
        self.date_time = date_time

    def display_activity_details(self):
        """Display the activity details."""
        print(f"Activity Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Cost: ${self.cost:.2f}")
        print(f"Date and Time: {self.date_time}")

def get_float_input(prompt):
    """Prompt for a float input and validate it."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("ERROR! Please enter a valid number.")

def add_activity():
    """Function to prompt user for activity details and create an Activity object."""
    name = input("Enter the name of the activity: ")
    description = input("Enter a description of the activity: ")
    cost = get_float_input("Enter the cost of the activity: ")
    date_time = input("Enter the date and time of the activity (YYYY-MM-DD HH:MM): ")

    # Create an Event object
    new_activity = Activity(name, description, cost, date_time)
    print("\nActivity Created Successfully!")
    new_activity.display_activity_details()

# Example usage
if __name__ == "__main__":
    add_activity()
