class Human:

    def __init__(self, name, weight, height):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("Run method")
        if self.height > 170:
            return self.height / 5
        return self.height / 10

    def eat(self):
        return self.weight / 10


human = Human("Manas", 61, 175)

print(human.name)
print(human.weight)
print(human.height)
print(human.run())
print(human.eat())
human2 = Human("Adilet1", 110, 150)
print()
print(human2.name)
print(human2.weight)
print(human2.height)
print(human2.run())
print(human2.eat())
