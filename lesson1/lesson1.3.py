class Home:

    def __init__(self, foundation, walls, rooftop, floor, ceiling):
        self.foundation = foundation
        self.walls = walls
        self.rooftop = rooftop
        self.floor = floor
        self.ceiling = ceiling

    def paint_walls(self, color):
        self.walls = color

    def paint_ceiling(self, color):
        self.ceiling = color

    def add_home(self, home):
        pass

    def show_house(self):
        return f"walls -> {self.walls}"


daniiars_house = Home(foundation="beton", walls="black", rooftop="black", floor="black", ceiling="black")
print("Daniiars " + daniiars_house.ceiling)
print("Daniiars " + daniiars_house.walls)
print("Daniiars " + daniiars_house.rooftop)
print("Daniiars " + daniiars_house.floor)
print("Daniiars " + daniiars_house.foundation)
sultan_house = Home("Wood", "pink", "pink", "pink", "pink")
print()
print("Sultans " + sultan_house.ceiling)
print("Sultans " + sultan_house.walls)
print("Sultans " + sultan_house.rooftop)
print("Sultans " + sultan_house.floor)
print("Sultans " + sultan_house.foundation)

daniiars_house.paint_walls("green")
sultan_house.paint_walls("orage")
print()
print("Daniiars walls " + daniiars_house.walls)
print("Sultans walls " + sultan_house.walls)

daniiars_house.paint_ceiling("green")
sultan_house.paint_ceiling("orage")
print()
print("Daniiars ceiling " + daniiars_house.walls)
print("Sultans ceiling " + sultan_house.walls)

# daniiars_house.add_home(sultan_house)
