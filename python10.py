# bank_account.py

"""
Bank Account Management System Demo
Demonstrates:
- Classes, constructors, attributes, methods
- Encapsulation (private attributes)
- Inheritance
- Method overriding
- Creating multiple objects
- Realistic bank operations (deposit, withdraw, transfer)
"""

# ---------- Base Class ----------
class BankAccount:
    """Base class for a bank account"""

    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number      # public attribute
        self.account_holder = account_holder      # public attribute
        self.__balance = balance                  # private attribute (encapsulation)

    # ---------- Methods ----------
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")

    def get_balance(self):
        """Getter method for private balance attribute"""
        return self.__balance

    def account_info(self):
        """Display account details"""
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance       : {self.__balance}")

# ---------- Derived Class ----------
class SavingsAccount(BankAccount):
    """Derived class for savings account with interest"""

    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    # 6. Override method to include interest info
    def account_info(self):
        super().account_info()
        print(f"Interest Rate : {self.interest_rate * 100}%")

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")

# ---------- Derived Class ----------
class CheckingAccount(BankAccount):
    """Derived class for checking account with overdraft limit"""

    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    # Override withdraw to allow overdraft
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > (self.get_balance() + self.overdraft_limit):
            print("Exceeded overdraft limit!")
        else:
            # Access private balance via getter + internal adjustment
            new_balance = self.get_balance() - amount
            # Normally we would use setter, but we can simulate via deposit/withdraw
            # For simplicity, directly adjust using deposit(-amount)
            self._BankAccount__balance = new_balance
            print(f"{amount} withdrawn. New balance: {self.get_balance()}")

# ---------- Bank Operations ----------
def transfer(sender, receiver, amount):
    """Simulate money transfer between two accounts"""
    print(f"\nTransferring {amount} from {sender.account_holder} to {receiver.account_holder}")
    if amount <= 0:
        print("Transfer amount must be positive.")
        return
    if sender.get_balance() >= amount:
        sender.withdraw(amount)
        receiver.deposit(amount)
        print("Transfer successful!")
    else:
        print("Insufficient balance for transfer!")

# ---------- Main Program ----------
if __name__ == "__main__":
    # 7. Create multiple objects
    acc1 = SavingsAccount("SA101", "Alice", 1000)
    acc2 = CheckingAccount("CA201", "Bob", 500)

    # Display account info
    print("\n--- Account Details ---")
    acc1.account_info()
    print()
    acc2.account_info()

    # 8. Simulate real bank operations
    print("\n--- Bank Transactions ---")
    acc1.deposit(200)
    acc2.withdraw(100)
    acc1.add_interest()

    transfer(acc1, acc2, 300)

    print("\n--- Updated Account Details ---")
    acc1.account_info()
    print()
    acc2.account_info()
