class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} into account. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from account. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

account = BankAccount("3333", "mahmood")

account.deposit(1000)

account.withdraw(500)

print(f"Current balance: {account.get_balance()}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} applied. New balance: {self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"

savings_account = SavingsAccount("2223", "yousha", 0.05)

savings_account.apply_interest()

print(savings_account)
