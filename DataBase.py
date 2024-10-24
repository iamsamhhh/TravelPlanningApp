from sqlitedict import SqliteDict
from DataStorage import *
from TravelPlan import *

# # Save data using a key to a SQLite database
# def save(key, value, cache_file="data.sqlite3"):
#     try:
#         with SqliteDict(cache_file) as mydict:
#             mydict[key] = value # Store the value using the key
#             mydict.commit() # Commit to flush the data to disk
#     except Exception as ex:
#         print("Error during storing data (Possibly unsupported):", ex)

# # Retrieve stored data using the key from the SQLite database
# def load(key, cache_file="data.sqlite3"):
#     try:
#         with SqliteDict(cache_file) as mydict:
#             value = mydict[key] # Retrieve the value using the key
#         return value
#     except Exception as ex:
#         print("Error during loading data:", ex)

# # Check if a user exists in the database
# def UserExist(key):
#     try:
#         with SqliteDict("data.sqlite3") as mydict:
#             for i in mydict.keys():
#                 if i == key:
#                     return True
#             return False
#     except Exception as ex:
#         print("Error during searching data:", ex)

# Class to store and manage user data
class UserData:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.travelPlanList = []
        self.Save()
    
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

    # Save the user data to the database
    def Save(self):
        save(self.userName, self)
