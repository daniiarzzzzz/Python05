class BankAccount:

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance


account = BankAccount(1, 90)
account._balance = -9999
# Cчет пользователя {self._balance}
print(account._balance)
print(account._name)
