'''
Mini Project: Bank Management System

We will build a simple bank system where:
A user can create an account
Deposit or withdraw money
Check balance
Bank can have multiple account holders
We use inheritance to create SavingsAccount and CurrentAccount
'''

# Parent Class
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # Encapsulation: private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def display_info(self):
        print(f"Account holder: {self.name}")
        print(f"Balance: {self.__balance}")


# Child Class (Inheritance + Polymorphism)
class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.03):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest of {interest} applied.")


class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=1000):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.get_balance() + self.overdraft_limit:
            self._BankAccount__balance -= amount  # Accessing private variable
            print(f"{amount} withdrawn. Remaining balance: {self.get_balance()}")
        else:
            print("Overdraft limit exceeded.")


# Using the classes
print("=== Bank Management System ===")
acc1 = SavingsAccount("Alice", 1000)
acc1.display_info()
acc1.deposit(500)
acc1.withdraw(300)
acc1.apply_interest()
acc1.display_info()

print("\n---\n")

acc2 = CurrentAccount("Bob", 500)
acc2.display_info()
acc2.withdraw(1300)  # within overdraft
acc2.withdraw(300)   # exceeds limit
acc2.display_info()

'''
Concept	              Where it's used
---------------------------------------------------------------------
Class & Object	      BankAccount, SavingsAccount, CurrentAccount
Constructor	          __init__() in each class
Encapsulation	        __balance is private
Inheritance	          SavingsAccount and CurrentAccount inherit from BankAccount
Polymorphism	        withdraw() method behaves differently in each child class
Method Overriding	    withdraw() is overridden in CurrentAccount
'''