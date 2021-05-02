class Animal:

    def __init__(self, paroda, semeistvo):
        self.paroda = paroda
        self.semeistvo = semeistvo

    def eat(self):
        return self.paroda


class Popugai(Animal):

    def __init__(self, paroda, semeistvo, vid):
        super(Popugai, self).__init__(paroda, semeistvo)
        self.vid = vid


class Kakadu(Popugai):

    def __init__(self, paroda, semeistvo, vid, color):
        super(Kakadu, self).__init__(paroda, semeistvo, vid)
        self.color = color

    def eat(self):
        return self.paroda + self.color


class AraKakadu(Kakadu):

    def __init__(self, paroda, semeistvo, vid, color, kluv):
        super(AraKakadu, self).__init__(paroda, semeistvo, vid, color)
        self.kluv = kluv
