class BankAccount:
    count = 0

    def __init__(self, name):
        self.account_holder = name
        self.balance = 0
        BankAccount.count += 1
        self.account_number = BankAccount.count

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other):
        if amount <= self.balance:
            self.balance -= amount
            other.balance += amount
        else:
            print("Insufficient balance")


a1 = BankAccount("Samruddhi")
a2 = BankAccount("Siddhi")

a1.deposit(5000)
a2.deposit(3000)

a1.withdraw(1000)
a1.transfer(1000, a2)

a1.display_balance()
a2.display_balance()