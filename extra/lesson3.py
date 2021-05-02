class Human:

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        return f"Name - {self.name}; Age - {self.age}; Color - {self.color}"

    def __repr__(self):
        return f"Name - {self.name}; Age - {self.age}; Color - {self.color}"

    def __add__(self, other):
        return Human(
            self.name + " " + other.name,
            self.age + other.age,
            self.color + " " + other.color,
        )


h = Human("Adilya", 18, "black")
h2 = Human("Daniiar", 20, "yellow")
print(h)
print(h2)

l = [h, h2]
d = {"h": h}
print(l)
print(d)
h3 = h + h2
print(h3)
