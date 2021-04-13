class Electric:

    def fix_cables(self):
        return f"Fix {self.electronika}"


class CleaningCompany:

    def clean_window(self):
        return f"Clean windows"


class Office(Electric, CleaningCompany):

    def __init__(self, bolyar, project, electronika):
        self.dispenser = bolyar
        self.project = project
        self.electronika = electronika


class Home(Electric, CleaningCompany):

    def __init__(self, tv, konyar, electronika):
        self.tv = tv
        self.konayr = konyar
        self.electronika = electronika

    def __str__(self):
        return f"{self.tv}, {self.konayr} {self.electronika}"


class Garage:

    def __init__(self, car):
        self.car = car


home = Home(105, True, "Cables of home")
print(home)
print(home.fix_cables())
