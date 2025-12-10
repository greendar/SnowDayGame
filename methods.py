#methods.py
startingScore = 10


class Player:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.score = startingScore
        self.votesList = []
