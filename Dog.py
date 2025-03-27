import code


class Dog:
    def __init__(self, name, age, weight):
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
        return Dog(self.name + "_" + other.name, self.age + other.age, self.weight + other.weight)

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
        else:
            return False




