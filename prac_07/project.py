import datetime


class Project:
    def __init__(self, name, data, priority, estimate, percentage):
        self.name = name
        self.data = data
        self.priority = priority
        self.estimate = estimate
        self.percentage = percentage

    def __repr__(self):
        return f"{self.name}, start: {self.data}, priority {self.priority}, " \
               f"estimate: ${self.estimate}, completion: {self.percentage}%"

    def __lt__(self, other):
        return self.priority < other.priority

    def compare_data(self, data):
        data_compared = datetime.datetime.strftime(data, "%Y-%m-%d")
        self.data = datetime.datetime.strftime(self.data, "%Y-%m-%d")
        return self.data >= data_compared

    def check_completion(self):
        return self.percentage == 100

