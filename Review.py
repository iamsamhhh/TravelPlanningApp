# Review class for stroing a review
class Review:
    # Initialize review
    def __init__(self, place, userName, title, description):
        self.place = place
        self.userName = userName
        self.title = title
        self.description = description
    
    # Display review title, author and description
    def DisplayReview(self):
        print(self.title)
        print(f"By {self.userName}")
        print(self.description+"\n")