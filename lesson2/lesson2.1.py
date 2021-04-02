class Animal:

    def __init__(self, eyes, tongue, ears):
        self.eyes = eyes
        self.tongue = tongue
        self.ears = ears

    # def run(self):
    #     return f"Run ->"

    def eat(self):
        return "Eat"


class Donkey(Animal):

    def __init__(self, eyes, tongue, ears, tail):
        super(Donkey, self).__init__(eyes, tongue, ears)
        self.tail = tail

    def run(self):
        return "Run <- Donkey"

    def eat(self):
        return "Eat Grass"


class Eshek(Donkey):

    def __init__(self, eyes, tongue, ears, tail, stamina):
        super(Eshek, self).__init__(eyes, tongue, ears, tail)
        self.stamina = stamina

    # def run(self):
    #     return "Run gallop Eshek"


class Osyol(Donkey):

    def __init__(self, eyes, tongue, ears, tail, stubborn):
        super(Osyol, self).__init__(eyes, tongue, ears, tail)
        self.stubborn = stubborn

    def run(self):
        return "Run zigzag Osyol"

    def scream(self):
        return "Scream"


donkey = Donkey("big", "long", "big", "short")
print(donkey.run())
print(donkey.eat())

osyol = Osyol("big", "long", "big", "short", True)
print(osyol.run())
print(osyol.eat())
