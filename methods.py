#methods.py
startingScore = 10


class Player:
    def __init__(self, email, name):
        self.email = email
        self.name = name
        self.score = startingScore
        self.votesList = []


class SnowDay:   
    def __init__(self, date):
        """
        Docstring for __init__       
        :param date: Date format "2025-12-10"
        """
        from datetime import datetime
        pass



'''from datetime import datetime

# Example date
date_str = "2025-12-10"
date_obj = datetime.strptime(date_str, "%Y-%m-%d")

# Get day of the week
day_of_week = date_obj.strftime("%A")
print(day_of_week)  # Output: Wednesday'''