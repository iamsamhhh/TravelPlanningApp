class Review:
    def __init__(self, place, userName, title, description):
        self.place = place
        self.userName = userName
        self.title = title
        self.description = description
    
    def DisplayReview(self):
        print(self.title)
        print(f"By {self.userName}")
        print(self.description+"\n")