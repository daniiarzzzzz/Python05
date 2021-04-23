import sqlite3

connection = sqlite3.connect("db.sqlite3")


class Car:

    def __init__(self, mark, model, volume, year, color):
        self.mark = mark
        self.model = model
        self.volume = volume
        self.year = year
        self.color = color

    def save(self):
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?, ?)",
                       (self.mark, self.model, self.volume, self.year, self.color))


car = Car("Ford", "Mondeo", 1.8, 2003, 'gold')
car.save()
car2 = Car("Honda", "Bit", 0.5, 2009, 'white')
car2.save()