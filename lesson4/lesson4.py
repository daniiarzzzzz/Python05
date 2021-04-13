class Human:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def get_class(cls):
        return cls

    @staticmethod
    def a_b(a, b):
        return a + b

    @property
    def name(self):
        return f"My name is {self._name}"

    @name.setter
    def name(self, name):
        if name in ["Daniiar"]:
            return
        self._name = name

    @property
    def kek(self):
        if self._name == "Tilek":
            return "Tilek's kek"
        return "kek"


human = Human("Tilek", 17)
human.name = "Daniiar"
print(human.name)
print(human.kek)
print(Human.get_class())

