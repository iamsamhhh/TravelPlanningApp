class Event:
    def __init__(self, name, description, cost, date_time):
        """Initialize an event with its details."""
        self.name = name
        self.description = description
        self.cost = cost
        self.date_time = date_time

    def display_event_details(self):
        """Display the details of the event."""
        return (f"Event: {self.name}\n"
                f"Description: {self.description}\n"
                f"Cost: ${self.cost}\n"
                f"Date & Time: {self.date_time}\n")


class TravelPlan:
    def __init__(self):
        self.events = []  # List to hold events

    def add_event(self, event):
        """Adds an event to the travel plan."""
        self.events.append(event)

    def show_total_cost(self):
        """Calculates and returns the total cost of all events."""
        total_cost = sum(event.cost for event in self.events)
        return total_cost

    def display_timeline(self):
        """Displays all events in chronological order."""
        sorted_events = sorted(self.events, key=lambda x: x.date_time)
        for event in sorted_events:
            print(event.display_event_details())

    def delete_event(self, event_name):
        """Deletes an event by name."""
        for event in self.events:
            if event.name == event_name:
                self.events.remove(event)
                print(f"Event '{event_name}' deleted successfully.")
                return
        print(f"Event '{event_name}' not found.")


# Example Usage
if __name__ == "__main__":
    event1 = Event("Beach Trip", "Visit the beach for a day", 100, "2024-10-30 10:00")
    event2 = Event("Mountain Hike", "Hiking in the mountains", 150, "2024-11-01 08:00")

    travel_plan = TravelPlan()
    travel_plan.add_event(event1)
    travel_plan.add_event(event2)

    print(f"Total Cost: ${travel_plan.show_total_cost()}")
    travel_plan.display_timeline()
    travel_plan.delete_event("Beach Trip")
