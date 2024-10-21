import DataBase
import Travel
import Event

def main ():
    userData = UserRegistration()
    quitApp = False
    travel = Travel.Travel()
    haveTravelOpen = False
    # Main loop
    while not quitApp:
        input = UserInput()
        if input == "Create travel":
            travel = CreateTravel()
            haveTravelOpen = True
        elif input == "Show travel list":
            ShowTravelList()
        elif input == "Open travel":
            travel = OpenTravel()
            haveTravelOpen = True
        elif haveTravelOpen and input == "Close travel":
            haveTravelOpen = False
            travel = Travel.Travel()
        elif haveTravelOpen and input == "Add event":
            AddEvent(travel)
        elif input == "Quit":
            quitApp = True
        

def OpenTravel():
    return Travel.Travel()

def ShowTravelList():
    print("Travel list")
        
# TODO: function and class to create travel that record cost, timeline, tickets & hotel info.
def CreateTravel():
    return Travel.Travel()

# TODO: function and class to create an event to add in travel. Event should include cost, time and description.(tickets if any)
def AddEvent(travel):
    event = Event.Event()
    travel.AddEvent(event)

# TODO: validate user input and return the input.(Valid input: Create travel, )
def UserInput():
    return ""

def UserRegistration():
    userNew = input("Are you new to Travel planning app? (yes/no):")
    if userNew == "yes":
        return UserSignUp()
    else:
        userName = input("Enter user name")
        password = input("Enter password")
        data = DataBase.load(userName)
        if data.password == password:
            print("logged in!")
            return data
        else:
            while password != data.password:
                password = input("Password incorrect!Enter password")
            print("logged in!")
            return data


def UserSignUp():
    userName = input("Enter user name")
    password = input("Enter password")
    return DataBase.UserData(userName, password)
    

if __name__ == '__main__':
    main()