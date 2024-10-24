# {place : [review1, review2...]}
from sqlitedict import SqliteDict
from DataBase import save
from DataBase import load

class Review:
    def __init__(self, place, userName, title, description):
        self.place = place
        self.userName = userName
        self.title = title
        self.description = description
    
    def DisplayReview(self):
        print(self.title)
        print(f"By {self.userName}")
        print(self.description)

reviewDict = {}

def AddReview(review):
    for key in reviewDict.keys():
        if key == review.place:
            reviewDict[review.place].append(review)
            return
    reviewDict[review.place] = []
    reviewDict[review.place].append(review)
    
def ShowReview(place):
    reviews = reviewDict[place]
    for review in reviews:
        review.DisplayReview()
        print("")

def SaveReview():
    save("Reviews", reviewDict, "Reviews.sqlite3")

def LoadReview():
    return load("Reviews", "Reviews.sqlite3")

if __name__ == "__main__":
    reviewDict = LoadReview()
    ShowReview("ShenZhen")