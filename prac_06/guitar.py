"""
Guitar class
"""

CURRENT_YEAR = 2022


class Guitar:
    """ Consist of guitar details """
    def __init__(self, name="", year=0, cost=0):
        """ Initialisation of guitar """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """ return string representation of a guitar """
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """ Calculate the age of a guitar according to current year """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """ Determine if a guitar is considered to be vintage """
        return self.get_age() >= 50

    def __lt__(self, other):
        """ Less than, used for sorting guitar """
        return self.year < other.year
