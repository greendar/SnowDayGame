#objects.py
startingScore = 10


class Player:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.score = startingScore
        self.votesList = []


class SnowDay:   
    def __init__(self, date_str):
        """
        Docstring for __init__       
        :param date: Date format "2025-12-10"
        """
        from methods import dayOfWeek
        self.date_str = date_str
        self.day = dayOfWeek(self.date_str)


