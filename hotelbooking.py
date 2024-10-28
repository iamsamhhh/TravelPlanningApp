import json
from datetime import datetime, timedelta

class HotelBookingSystem:
    def __init__(self):
        # Initialize hotel data structure using dictionary
        self.rooms = {
            'standard': {'total': 10, 'price': 100, 'available': 10},
            'deluxe': {'total': 5, 'price': 200, 'available': 5},
            'suite': {'total': 3, 'price': 300, 'available': 3}
        }
        self.bookings = []
        self.load_data()

    def load_data(self):
        """Load existing booking data from file"""
        try:
            with open('bookings.json', 'r') as file:
                self.bookings = json.load(file)
        except FileNotFoundError:
            self.bookings = []

    def save_data(self):
        """Save booking data to file"""
        with open('bookings.json', 'w') as file:
            json.dump(self.bookings, file)

    def display_available_rooms(self):
        """Display current room availability"""
        print("\n=== Available Rooms ===")
        for room_type, details in self.rooms.items():
            print(f"{room_type.title()} Room:")
            print(f"  Available: {details['available']}/{details['total']}")
            print(f"  Price per night: ${details['price']}")

    def make_booking(self, guest_name, room_type, check_in, check_out):
        """Process a new booking"""
        if room_type not in self.rooms:
            return False, "Invalid room type"
        
        if self.rooms[room_type]['available'] <= 0:
            return False, "No rooms available for this type"

        # Calculate total price
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        nights = (check_out_date - check_in_date).days
        total_price = self.rooms[room_type]['price'] * nights

        # Create booking
        booking = {
            'booking_id': len(self.bookings) + 1,
            'guest_name': guest_name,
            'room_type': room_type,
            'check_in': check_in,
            'check_out': check_out,
            'total_price': total_price
        }

        self.bookings.append(booking)
        self.rooms[room_type]['available'] -= 1
        self.save_data()
        return True, booking

    def cancel_booking(self, booking_id):
        """Cancel an existing booking"""
        for booking in self.bookings:
            if booking['booking_id'] == booking_id:
                self.rooms[booking['room_type']]['available'] += 1
                self.bookings.remove(booking)
                self.save_data()
                return True, "Booking cancelled successfully"
        return False, "Booking not found"

def main():
    hotel = HotelBookingSystem()
    
    while True:
        print("\n=== Hotel Booking System ===")
        print("1. View Available Rooms")
        print("2. Make a Booking")
        print("3. Cancel Booking")
        print("4. View All Bookings")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            hotel.display_available_rooms()
            
        elif choice == '2':
            guest_name = input("Enter guest name: ")
            print("\nRoom Types: standard, deluxe, suite")
            room_type = input("Enter room type: ").lower()
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")
            
            success, result = hotel.make_booking(guest_name, room_type, check_in, check_out)
            if success:
                print("\nBooking Confirmed!")
                print(f"Booking ID: {result['booking_id']}")
                print(f"Total Price: ${result['total_price']}")
            else:
                print(f"\nError: {result}")
                
        elif choice == '3':
            booking_id = int(input("Enter booking ID to cancel: "))
            success, message = hotel.cancel_booking(booking_id)
            print(message)
            
        elif choice == '4':
            print("\n=== All Bookings ===")
            for booking in hotel.bookings:
                print(f"\nBooking ID: {booking['booking_id']}")
                print(f"Guest: {booking['guest_name']}")
                print(f"Room Type: {booking['room_type']}")
                print(f"Check-in: {booking['check_in']}")
                print(f"Check-out: {booking['check_out']}")
                print(f"Total Price: ${booking['total_price']}")
                
        elif choice == '5':
            print("Thank you for using the Hotel Booking System!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

