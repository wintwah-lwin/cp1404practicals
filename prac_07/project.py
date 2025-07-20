from datetime import datetime

from datetime import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """initialize variables"""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date() if isinstance(start_date, str) else start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        """string output"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")

    def is_complete(self):
        """completion percentage"""
        return self.completion == 100

    def update(self, completion=None, priority=None):
        """update percent and priority"""
        if completion != "":
            self.completion = int(completion)
        if priority != "":
            self.priority = int(priority)

    def __lt__(self, other):
        """sort project according to priority"""
        return self.priority < other.priority
