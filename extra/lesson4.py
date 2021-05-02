class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != "1":
            print("Нельзя поставить значение")
        else:
            self._name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance can't be lower than 0")
        else:
            self._balance = value


b = BankAccount("1", 150)
b.name = "1"
b.balance = 1500
print(b.balance)
print(b.name)
