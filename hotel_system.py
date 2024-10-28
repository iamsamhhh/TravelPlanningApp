import json
from datetime import datetime

class HotelSystem:
    def __init__(self):
        # REQUIREMENT: Collection type (dictionary and list) to store and manage data
        self.rooms = {
            'standard': {'price': 100, 'available': 5},
            'deluxe': {'price': 200, 'available': 3}
        }
        self.bookings = []  # List to store bookings
        self.load_data()

    # REQUIREMENT: File input
    def load_data(self):
        """Load booking data from file"""
        try:
            with open('hotel_data.json', 'r') as file:
                self.bookings = json.load(file)
            print("Data loaded successfully!")
        except FileNotFoundError:
            print("No existing data found. Starting fresh.")

    # REQUIREMENT: Subroutine with parameters and return type
    def create_booking(self, guest_name: str, room_type: str, nights: int) -> tuple:
        """
        Create a new booking
        Parameters:
            guest_name (str): Name of the guest
            room_type (str): Type of room
            nights (int): Number of nights
        Returns:
            tuple: (success_status, result_message)
        """
        # Input validation
        if room_type not in self.rooms:
            return False, "Invalid room type"
        
        if self.rooms[room_type]['available'] <= 0:
            return False, "No rooms available"

        # Calculate total price
        total_price = self.rooms[room_type]['price'] * nights

        # Create booking
        booking = {
            'id': len(self.bookings) + 1,
            'guest': guest_name,
            'room': room_type,
            'nights': nights,
            'total': total_price
        }

        # Update system
        self.bookings.append(booking)
        self.rooms[room_type]['available'] -= 1
        
        # Save to file
        with open('hotel_data.json', 'w') as file:
            json.dump(self.bookings, file)
            
        return True, booking

def main():
    # Initialize system
    hotel = HotelSystem()
    
    # REQUIREMENT: Iteration (main program loop)
    while True:
        # REQUIREMENT: Output (textual) - Menu display
        print("\n=== Hotel Booking System ===")
        print("1. View Rooms")
        print("2. Make Booking")
        print("3. View Bookings")
        print("4. Exit")
        
        # REQUIREMENT: User input
        choice = input("\nSelect an option (1-4): ")
        
        # REQUIREMENT: Selection (if-elif structure)
        if choice == '1':
            # Display available rooms
            print("\nAvailable Rooms:")
            for room_type, info in hotel.rooms.items():
                print(f"{room_type.title()}: {info['available']} rooms at ${info['price']}/night")
                
        elif choice == '2':
            # REQUIREMENT: Sequencing (multiple inputs in sequence)
            guest_name = input("Enter guest name: ")
            print("\nRoom types: standard, deluxe")
            room_type = input("Enter room type: ").lower()
            nights = int(input("Enter number of nights: "))
            
            # REQUIREMENT: Call to student-developed procedure
            success, result = hotel.create_booking(guest_name, room_type, nights)
            
            # REQUIREMENT: Output based on input
            if success:
                print("\nBooking Confirmed!")
                print(f"Booking ID: {result['id']}")
                print(f"Total Cost: ${result['total']}")
            else:
                print(f"\nError: {result}")
                
        elif choice == '3':
            if not hotel.bookings:
                print("\nNo bookings found.")
            else:
                print("\nCurrent Bookings:")
                for booking in hotel.bookings:
                    print(f"\nID: {booking['id']}")
                    print(f"Guest: {booking['guest']}")
                    print(f"Room: {booking['room']}")
                    print(f"Nights: {booking['nights']}")
                    print(f"Total: ${booking['total']}")
                
        elif choice == '4':
            print("Thank you for using the Hotel Booking System!")
            break
            
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
