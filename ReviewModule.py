# {place : [review1, review2...]}
from sqlitedict import SqliteDict

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

if __name__ == "__main__":
    AddReview(
        Review("ShenZhen", "iamsam", "Come to ShenZhen!", 
               "ShenZhen is a good place with lots of shopping malls and food delivery all over the city!")
    )
    AddReview(
        Review("ShenZhen", "iamsam", "Don't come to ShenZhen!", 
               "ShenZhen is a bad place with lots of shopping malls and lots of people!")
    )
    ShowReview("ShenZhen")
    