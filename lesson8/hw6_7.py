import sqlite3

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()


class Car:

    def __init__(self, mark, model, volume, year, color, id):
        self.id = id
        self.mark = mark
        self.model = model
        self.volume = volume
        self.year = year
        self.color = color

    def save(self):
        cursor.execute(f"INSERT INTO cars values (?, ?, ?, ?, ?)",
                       (self.mark, self.model, self.volume, self.year, self.color))
        connection.commit()

    def link(self, cls):
        pass


class Retailer:

    def __init__(self, name, address, id):
        self.name = name
        self.address = address
        self.id = id

    def save(self):
        try:
            cursor.execute(f"INSERT INTO retailers values (?, ?, ?)",
                           (self.name, self.address, self.id))
            connection.commit()

        except Exception:
            # CREATE TABLE
            cursor.execute("")
            cursor.execute(f"INSERT INTO retailers values (?, ?, ?)",
                           (self.name, self.address, self.id))
            connection.commit()


car = Car("Ford", "Mondeo", 1.8, 2003, 'gold', 1)
car.save()
car2 = Car("Honda", "Bit", 0.5, 2009, 'white', 2)
car2.save()
r = Retailer("Honda Center", "Bishkek", 1)
car.link(r)
