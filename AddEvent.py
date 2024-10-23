class Event:
    def __init__(self, name, description, cost, date_time):
        """Initialize the event with the given details."""
        self.name = name
        self.description = description
        self.cost = cost
        self.date_time = date_time

    def display_event_details(self):
        """Display the event details."""
        print(f"Event Name: {self.name}")
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

def add_event():
    """Function to prompt user for event details and create an Event object."""
    name = input("Enter the name of the event: ")
    description = input("Enter a description of the event: ")
    cost = get_float_input("Enter the cost of the event: ")
    date_time = input("Enter the date and time of the event (YYYY-MM-DD HH:MM): ")

    # Create an Event object
    new_event = Event(name, description, cost, date_time)
    print("\nEvent Created Successfully!")
    new_event.display_event_details()

# Example usage
if __name__ == "__main__":
    add_event()
