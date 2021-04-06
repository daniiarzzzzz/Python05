class Engine:

    def __init__(self, hp, volume):
        self.hp = hp
        self.volume = volume

    def __str__(self):
        return f"Hp: {self.hp}\n Volume: {self.volume}"


class Wheels:

    def __init__(self, diameter, season, protector, disk):
        self.diameter = diameter
        self.season = season
        self.protector = protector
        self.disk = disk

    def __str__(self):
        return f"diameter: {self.diameter}\nseason: {self.season}\nprotector: {self.protector}\ndisk: {self.disk}"


class Carcase:

    def __init__(self, material, format, color):
        self.material = material
        self.format = format
        self.color = color

    def __str__(self):
        return f"Material: {self.material}\n Format: {self.format} Color: {self.color}"


class Car:

    def __init__(self, wheels, engine, carcase):
        self.wheels = wheels
        self.engine = engine
        self.carcase = carcase

    def __str__(self):
        return f"Wheel: [{self.wheels}]\n\nEngine: [{self.engine}]\n\nCarcase: [{self.carcase}]"


wheel = Wheels(14, "summer", "bold", "mattovyi")
print(wheel)
print()
engine = Engine(1500, 6)
carcase = Carcase("gold", "sedan", "glyanec")
car = Car(wheel, engine, carcase)
print()
print(car)
