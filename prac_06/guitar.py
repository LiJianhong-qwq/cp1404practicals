class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = 0

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __repr__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        age = 2023 - int(self.year)
        self.age = int(age)
        return age

    def is_vintage(self):
        if self.age >= 50:
            return True
        else:
            return False

