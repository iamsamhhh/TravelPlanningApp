from sqlitedict import SqliteDict
from DataStorage import *
from TravelPlan import *

# Class to store and manage user data
class UserData:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.travelPlanList = []
    
    # Add a new travel plan to the user's list
    def AddTravelPlan(self, travelPlan):
        for item in self.travelPlanList:
            if item.name == travelPlan.name:
                print(f"Travel plan with name '{travelPlan.name}' already exists!")
                return
        self.travelPlanList.append(travelPlan)
        print(f"Travel plan '{travelPlan.name}' added successfully.")

    # Delete a travel plan from the user's list
    def DeleteTravelPlan(self, travelPlanName):
        for travelPlan in self.travelPlanList:
            if travelPlan.name == travelPlanName:
                self.travelPlanList.remove(travelPlan)
                print(f"Travel plan '{travelPlanName}' deleted successfully.")
                return
        print(f"Travel plan '{travelPlanName}' not found.")
    
    # Get a travel plan by name. Return None if not found.
    def GetTravelPlan(self, travelPlanName):
        for travelPlan in self.travelPlanList:
            if travelPlan.name == travelPlanName:
                return travelPlan
        print(f"Travel plan '{travelPlanName}' not found.")
        return None  # Added to explicitly return None when not found
    
    # Check if a travel plan exists in the user's list
    def TravelPlanExist(self, travelPlanName):
        for travelPlan in self.travelPlanList:
            if travelPlan.name == travelPlanName:
                return True
        return False

    # Check if user already exists
    def Exist(self):
        try:
            with SqliteDict("data.sqlite3") as mydict:
                for i in mydict.keys():
                    if i == self.userName:
                        return True
                return False
        except Exception as ex:
            print("Error during searching data:", ex)
    
    # Load user data from database(file)
    def Load(self):
        if self.Exist():
            data = load(self.userName)
            self.password = data.password
            self.travelPlanList = data.travelPlanList
            return True
        else:
            return False

    # Save the user data to the database
    def Save(self):
        save(self.userName, self)
