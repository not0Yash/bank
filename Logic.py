
class Account:
    numAccounts = 0
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.logs = []
        Account.numAccounts += 1
    def deposit(self, amount):
        self.balance += amount
        self.logs.append(f"{self.name} deposited {amount} to their bank account")
    def withdraw(self, amount):
        self.balance -= amount
        self.logs.append(f"{self.name} withdrew {amount} from their bank account")
    def give_logs(self):
        print(f"Here is all the bank activity in {self.name}\' account\n")
        for i in range(len(self.logs)):
            print(self.logs[i] + "\n")
    def get_Bank(self):
        print(f"{self.name}\'s bank account has {self.balance} in their bank account")

a1 = Account("jojo")
a1.deposit(3012)
print(Account.numAccounts)
print(a1.get_Bank())
a1.withdraw(1200)
print(a1.get_Bank())
a1.give_logs()

class login:
    account_login = {}
    accounts = {}
    def create(self, name, password):
        accout_login = {name, password}
        # this part of the code will help us get a variable to difine the account 
        letters = "abcdefghijklmnopqurtuvwxyz"
        numbers = "123456789"
        number2 = "123456789"
        number3 = "123456780"
        for i in range(26):
            for j in range(10):
                for k in range(10):
                    for n in range(10):
                        code = letters[i] + numbers[j] + number2[k] + number3[n]
                        unique = True
                        while()