class Bank(object):
    def __init__(self, name, number, password, balance):
        self.name = name
        self.number = number
        self.password = password
        self.balance = balance

    def showBalance(self):
        print("Your account balance is : ", self.balance)

    def withDraw(self, amount):
        print("Amount withdrawn : ", amount)
        print("Your account balace is : ", self.balance-amount)

    def deposit(self, amount):
        print("Amount diposited : ", amount)
        print("Your account balace is : ", self.balance+amount)

Arham = Bank("Arham", 121, "abc", 10000)
Arham.withDraw(200)