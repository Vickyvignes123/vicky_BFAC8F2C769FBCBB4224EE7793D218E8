class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number  # Private attribute
        self.__account_holder_name = account_holder_name  # Private attribute
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount

    def display_balance(self):
        return f"Account Number: {self.__account_number}, Account Holder: {self.__account_holder_name}, Balance: {self.__account_balance}"


# Create an instance of the BankAccount class
account1 = BankAccount("123456", "Alice", 1000)

# Deposit money
account1.deposit(500)

# Withdraw money
account1.withdraw(200)

# Display account balance
print(account1.display_balance())
