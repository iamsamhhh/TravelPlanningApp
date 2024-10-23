import DataBase
from TravelPlan import *
from Activity import *
from UserInput import *

# Entrance of the app
def main ():
    # Retrive user data
    userData = UserRegistration()
    quitApp = False
    # initialize travel plan to store the current travel plan editing
    travelPlan = TravelPlan()
    # boolean to check if there there is travel plan opened.
    haveTravelPlanOpened = False
    # Main loop
    while not quitApp:
        # Get the user's input and decide what to do
        userInput = UserInput()
        # Creates a new travel plan
        if userInput == "Create travel plan":
            travelPlan = CreateTravelPlan()
            haveTravelPlanOpened = True
        # Display list of travel plan
        elif userInput == "Show travel plan list":
            ShowTravelPlanList()
        # Open a travel plan
        elif userInput == "Open travel plan":
            travelPlan = OpenTravelPlan()
            haveTravelPlanOpened = True
        # Close a travel plan
        elif haveTravelPlanOpened and userInput == "Close travel plan":
            haveTravelPlanOpened = False
            travelPlan = TravelPlan()
        # adds an event into the travel plan opened
        elif haveTravelPlanOpened and userInput == "Add activity":
            AddActivity(travelPlan)
        elif userInput == "Quit":
            quitApp = True
        
# TODO: Open an existing travel plan
def OpenTravelPlan():
    return TravelPlan()

# TODO: show the list of travel plan user created
def ShowTravelPlanList():
    print("TravelPlan list")
        
# TODO: function and class to create travel plan that record cost, timeline, tickets & hotel info.
def CreateTravelPlan():
    return TravelPlan()

# TODO: function and class to create an event to add in travel. Activity should include cost, time and description.(tickets if any)
def AddActivity(travelPlan):
    activity = create_activity()
    travelPlan.add_activity(activity)

# Function to ask for user name and password and return user data
def UserRegistration():
    userNew = input("Are you new to travel planning app? (yes/no):")
    if userNew == "yes":
        return UserSignUp()
    else:
        userName = input("Enter user name: ")
        password = input("Enter password: ")
        # TODO: Check if user is signed up
        data = DataBase.load(userName)
        if data.password == password:
            print("logged in!")
            return data
        else:
            while password != data.password:
                password = input("Password incorrect! Enter password: ")
            print("logged in!")
            return data

# function to let user sign up account
def UserSignUp():
    userName = input("Enter user name: ")
    password = input("Enter password: ")
    return DataBase.UserData(userName, password)
    

if __name__ == '__main__':
    main()