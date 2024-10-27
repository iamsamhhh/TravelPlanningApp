from DataStorage import *
from sqlitedict import SqliteDict
from Review import *

# Class to store all review for one place
class Place:
    # initialize place
    def __init__(self, name):
        self.name = name
        self.reviews = []
    
    # Add a review into this place
    def AddReview(self, review):
        self.reviews.append(review)
    
    # Show all reviews of the place
    def ShowReview(self):
        print(f"Review for {self.name}:\n")
        if self.reviews != None:
            for review in self.reviews:
                review.DisplayReview()
    
    # Save the place into database
    def Save(self):
        save(self.name, self.reviews, "Reviews.sqlite3")
    
    # Load the place from data place
    def Load(self):
        if self.Exist():
            self.reviews = load(self.name, "Reviews.sqlite3")
            return True
        else:
            return False

    # Check if this place exist in database
    def Exist(self):
        try:
            with SqliteDict("Reviews.sqlite3") as mydict:
                for i in mydict.keys():
                    if i == self.name:
                        return True
                return False
        except Exception as ex:
            print("Error during searching data:", ex)

# Test
if __name__ == "__main__":
    place = Place("ShenZhen")
    if not place.Load():
        print("loading place review failed")
    # place.AddReview(
    #     Review("ShenZhen", "iamsam", "Come to ShenZhen!", 
    #            "ShenZhen is a good place with lots of shopping malls and food delivery all over the city!")
    # )
    place.ShowReview()
    place.Save()