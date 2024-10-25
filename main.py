import DataStorage
from DataBase import *
from TravelPlan import *
from Activity import *
import ReviewModule
from Review import Review

# Entrance of the app
def main():
    # Retrieve user data (login or register)
    userData = UserRegistration()
    quitApp = False
    # Boolean to check if there is a travel plan opened
    haveTravelPlanOpened = False
    travelPlan = TravelPlan("")
    # Main application loop
    while not quitApp:
        # Display current open travel plan, if any
        if haveTravelPlanOpened:
            print(f"Current travel plan opened: {travelPlan.name}")
        
        # Get the user's input and decide what action to take
        userInput = UserInput()

        # Handle different user inputs
        if userInput == "Create travel plan":
            name = input("Enter the name of the travel plan: ")
            if not userData.TravelPlanExist(name):  # Fixed: Pass 'name' instead of 'travelPlan'
                travelPlan = TravelPlan(name)
                userData.AddTravelPlan(travelPlan)
                userData.Save()
                haveTravelPlanOpened = True
            else:
                print(f"Travel plan '{name}' already exists!")
                
        elif userInput == "Show travel plan list":
            ShowTravelPlanList(userData)
        
        elif userInput == "Open travel plan":
            name = input("Enter the name of the travel plan to open: ")
            if userData.TravelPlanExist(name):
                travelPlan = userData.GetTravelPlan(name)
                haveTravelPlanOpened = True
            else:
                print(f"Travel plan '{name}' not found!")
        
        elif haveTravelPlanOpened and userInput == "Close travel plan":
            haveTravelPlanOpened = False
            userData.Save()
        
        elif haveTravelPlanOpened and userInput == "Add activity":
            AddActivity(travelPlan)
            userData.Save()

        elif haveTravelPlanOpened and userInput == "Show timeline":
            travelPlan.display_timeline()

        elif haveTravelPlanOpened and userInput == "Show total cost":
            print(f"Total cost of travel plan '{travelPlan.name}' is ${travelPlan.get_total_cost():.2f}")

        elif userInput == "Check review":
            placeName = input("Enter the place you want to look up reviews: ")
            place = ReviewModule.Place(placeName)
            if place.Exist():
                place.Load()
                place.ShowReview()
            else:
                print(f"There are currently no review for {placeName}.")

        elif userInput == "Add review":
            placeName = input("Enter the place you want to write a review: ")
            title = input("Enter the title of your review: ")
            text = input("Write your review:\n")
            place = ReviewModule.Place(placeName)
            place.Load()
            place.AddReview(Review(placeName, userData.userName, title, text))
            place.Save()

        elif userInput == "Quit":
            userData.Save()
            quitApp = True
        
        # Wait for user input before continuing
        input("Enter any key to continue...\n")

def UserInput():
    """Prompt for user input and validate it."""
    # Define valid actions
    valid_inputs = {
        "1": "Create travel plan",
        "2": "Show travel plan list",
        "3": "Open travel plan",
        "4": "Close travel plan",
        "5": "Add activity",
        "6": "Show timeline",
        "7": "Show total cost",
        "8": "Check review",
        "9": "Add review",
        "10": "Quit"
    }

    # Display the menu options
    print("Please select an option:")
    for key, value in valid_inputs.items():
        print(f"{key}: {value}")

    # Loop until a valid input is received
    while True:
        user_input = input("Enter the option number: ").strip()
        if user_input in valid_inputs:
            return valid_inputs[user_input]
        else:
            print("Invalid input. Please enter a valid option number.")


# Function to display the list of travel plans the user has created
def ShowTravelPlanList(userData):
    travelPlans = userData.travelPlanList
    for travelPlan in travelPlans:
        print(travelPlan.name)

# Function to add an activity to the current travel plan
def AddActivity(travelPlan):
    activity = create_activity()
    travelPlan.add_activity(activity)

# Function to handle user registration or login
def UserRegistration():
    userName = input("Enter user name: ")
    password = input("Enter password: ")
    data = UserData(userName, password)
    if data.Load():
        if data.password == password:
            print("Logged in!")
            return data
        else:
            while password != data.password:
                password = input("Password incorrect! Enter password: ")
            print("Logged in!")
            return data
    print(f"New account '{userName}' created with name password '{password}'.")
    data.Save()
    return data

# Entry point of the application
if __name__ == '__main__':
    main()
