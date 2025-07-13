

CURRENT_YEAR = 2025

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        "initialize Guitar"
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return string representation of Guitar"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """get age from guitar year"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """return true if guitar age is 50 or more"""
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.year < other.year
