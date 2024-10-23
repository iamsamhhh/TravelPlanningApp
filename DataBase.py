from sqlitedict import SqliteDict
from TravelPlan import *

# Save data using a key
def save(key, value, cache_file="data.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            mydict[key] = value # Using dict[key] to store
            mydict.commit() # Need to commit() to actually flush the data
    except Exception as ex:
        print("Error during storing data (Possibly unsupported):", ex)

# Returns the stored data using the key
def load(key, cache_file="data.sqlite3"):
    try:
        with SqliteDict(cache_file) as mydict:
            value = mydict[key] # No need to use commit(), since we are only loading data!
        return value
    except Exception as ex:
        print("Error during loading data:", ex)

def UserExist(key):
    try:
        with SqliteDict("data.sqlite3") as mydict:
            for i in mydict.keys():
                if i == key:
                    return True
            return False
    except Exception as ex:
        print("Error during searching data:", ex)

# This class stores the user data
class UserData:
    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.travelPlanList = []
    
    def load(self):
        rawData = load(self.userName)
        self.password = rawData.password
        for travelPlanName, activities in rawData.travelPlans.items():
            travelPlan = TravelPlan(travelPlanName)
            for activityName, (description, cost, date_time) in activities.items():
                travelPlan.add_activity(Activity(activityName, description, cost, date_time))
            self.travelPlanList.append(travelPlan)
        
    
    def AddTravelPlan(self, travelPlan):
        for item in self.travelPlanList:
            if item.name == travelPlan.name:
                print(f"Travel plan with name '{travelPlan.name}' already exist!")
                return
        self.travelPlanList.append(travelPlan)
        print(f"Travel plan '{travelPlan.name}' added succseefully.")

    def DeleteTravelPlan(self, travelPlanName):
        for travelPlan in self.travelPlanList:
            if travelPlan.name == travelPlanName:
                self.travelPlanList.remove(travelPlan)
                print(f"Tavel plan '{travelPlanName}' deleted successfully.")
                return
        print(f"Tavel plan '{travelPlanName}' not found.")
    
    '''Get travel plan by name. Return an empty travel plan if not found.'''
    def GetTravelPlan(self, travelPlanName):
        for travelPlan in self.travelPlanList:
            if travelPlan.name == travelPlanName:
                return travelPlan
        print(f"Tavel plan '{travelPlanName}' not found.")
    
    def TravelPlanExist(self, travelPlanName):
        for travelPlan in self.travelPlanList:
            if travelPlan.name == travelPlanName:
                return True
        return False

    def Save(self):
        save(self.userName, UserRawData(self))

class UserRawData:
    def __init__(self, userData):
        self.userName = userData.userName
        self.password = userData.password
        self.travelPlans = {}
        for i in userData.travelPlanList:
            activities = {}
            for j in i.activities:
                activities[j.name] = (j.description, j.cost, j.date_time)
            self.travelPlans[i.name] = activities

