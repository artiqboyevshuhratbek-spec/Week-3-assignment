class BankAccount:
    bank_name = "Urgench Bank"
    total_accounts = 0
    min_balance = 10

    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.balance = initial_balance
        BankAccount.total_accounts += 1
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
    def withdraw(self, amount):
        if (self.balance - amount) >= BankAccount.min_balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or below minimum balance")

    def display_account_info(self):
        print(f"Owner: {self.owner}, Balance: {self.balance}, Bank: {BankAccount.bank_name}")
account1 = BankAccount("Ali", 100)
account2 = BankAccount("Vali", 50)
account1.display_account_info()
account1.deposit(50)
account1.withdraw(80)
account2.display_account_info()
account2.withdraw(100)
print(f"Total accounts created: {BankAccount.total_accounts}")