import DataBase
from TravelPlan import *
from Activity import *
from UserInput import *

# Entrance of the app
def main ():
    # Retrive user data
    userData = UserRegistration()
    quitApp = False
    # boolean to check if there there is travel plan opened.
    haveTravelPlanOpened = False
    travelPlan = TravelPlan("")
    # Main loop
    while not quitApp:
        # Get the user's input and decide what to do
        userInput = UserInput()

        # Creates a new travel plan
        if userInput == "Create travel plan":
            name = input("Enter the name of the travel plan: ")
            if not userData.TravelPlanExist(travelPlan):
                travelPlan = TravelPlan(name)
                userData.AddTravelPlan(travelPlan)
                userData.Save()
                haveTravelPlanOpened = True
            else:
                print(f"Travel plan '{name}' already exist!")
                
        # Display list of travel plan
        elif userInput == "Show travel plan list":
            ShowTravelPlanList(userData)
        
        # Open a travel plan
        elif userInput == "Open travel plan":
            name = input("Enter the name of the travel plan to open: ")
            if userData.TravelPlanExist(name):
                travelPlan = userData.GetTravelPlan(name)
                haveTravelPlanOpened = True
            else:
                print(f"Travel plan '{name} not found!'")
        
        # Close a travel plan
        elif haveTravelPlanOpened and userInput == "Close travel plan":
            haveTravelPlanOpened = False
            userData.Save()
        
        # adds an event into the travel plan opened
        elif haveTravelPlanOpened and userInput == "Add activity":
            AddActivity(travelPlan)
            userData.Save()
        elif haveTravelPlanOpened and userInput == "Show timeline":
            travelPlan.display_timeline()
        elif userInput == "Quit":
            userData.Save()
            quitApp = True

# TODO: show the list of travel plan user created
def ShowTravelPlanList(userData):
    travelPlans = userData.travelPlanList
    for travelPlan in travelPlans:
        print(travelPlan.name)

# TODO: function and class to create an event to add in travel. Activity should include cost, time and description.(tickets if any)
def AddActivity(travelPlan):
    activity = create_activity()
    travelPlan.add_activity(activity)

# Function to ask for user name and password and return user data
def UserRegistration():
    userName = input("Enter user name: ")
    password = input("Enter password: ")
    if DataBase.UserExist(userName):
        data = DataBase.load(userName)
        if data.password == password:
            print("logged in!")
            return data
        else:
            while password != data.password:
                password = input("Password incorrect! Enter password: ")
            print("logged in!")
            return data
    else:
        data = DataBase.UserData(userName, password)
        return data
        

if __name__ == '__main__':
    main()