import DataStorage
from sqlitedict import SqliteDict
from DataBase import save
from DataBase import load
from Review import *

class Place:
    def __init__(self, name):
        self.name = name
        self.reviews = []
    
    def AddReview(self, review):
        self.reviews.append(review)
    
    def ShowReview(self):
        print(f"Review for {self.name}:\n")
        if self.reviews != None:
            for review in self.reviews:
                review.DisplayReview()
    
    def Save(self):
        save(self.name, self.reviews, "Reviews.sqlite3")
    
    def Load(self):
        if self.Exist():
            self.reviews = DataStorage.load(self.name, "Reviews.sqlite3")
            return True
        else:
            return False

    def Exist(self):
        try:
            with SqliteDict("Reviews.sqlite3") as mydict:
                for i in mydict.keys():
                    if i == self.name:
                        return True
                return False
        except Exception as ex:
            print("Error during searching data:", ex)

if __name__ == "__main__":
    place = Place("ShenZhen")
    if not place.Load():
        print("loading place review failed")
    # place.AddReview(
    #     Review("ShenZhen", "iamsam", "Come to ShenZhen!", 
    #            "ShenZhen is a good place with lots of shopping malls and food delivery all over the city!")
    # )
    # place.AddReview(
    #     Review("ShenZhen", "iamsam", "Don't come to ShenZhen!", 
    #            "ShenZhen is a bad place with lots of shopping malls and lots of people!")
    # )
    place.ShowReview()
    place.Save()