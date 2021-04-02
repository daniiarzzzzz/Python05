class Human:

    def __init__(self, skin_color, name, language):
        self.skin_color = skin_color
        self.name = name
        self.language = language

    def eat(self):
        return f"{self.name}, Im eating!"


class Russian(Human):

    def __init__(self, skin_color, name, language, bath):
        super(Russian, self).__init__(skin_color, name, language)
        self.bath = bath


class Kyrgyz(Human):

    def __init__(self, skin_color, name, language, revolutions):
        super(Kyrgyz, self).__init__(skin_color, name, language)
        self.revolutions = revolutions


class American(Human):

    def __init__(self, skin_color, name, language, fast_food):
        super(American, self).__init__(skin_color, name, language)
        self.fast_food = fast_food


russian = Russian("white", "Vanya", "rus", "wooden")
kyrgyz = Kyrgyz("yellow", "Manas", "kyr", "aprel")
american = American("white", "Sam", "eng", "burger")
print(russian.eat())
print(kyrgyz.eat())
print(american.eat())

