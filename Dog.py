class Dog:
    def __init__(self, name, age=0, weight=0):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self):
        if self.weight > 25:
            print(self.name + " says WOOF WOOF!")
        else:
            print(self.name + " says woof woof!")


    def __str__(self):
        return f"{self.name} is a Dog object, and its age is {self.age}, and its weight {self.weight}"

    def __abs__(self):
        return "canine"

    def __add__(self, other):
        if type(other) is Dog:
            return Dog(self.name + "_" + other.name, self.age + other.age, self.weight + other.weight)
        elif type(other) is int:
            return self.age + other + self.weight
        else:
            return self.age

    def __int__(self):
        return int(self.age + self.weight)

    def __eq__(self, other):
        if self.age == other.age and self.weight == other.weight:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.age >= other.age and self.weight >= other.weight:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.age < other.age:
            return True
        elif self.age == other.age and self.weight < other.weight:
            return True
        elif self.age == other.age and self.weight == other.weight and self.name < other.name:
            return True
        return False




