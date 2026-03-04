class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Amount deposited: {amount}"
        else:
            return "Deposit amount must be positive"
        
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Amount withdrawn: {amount}"

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")


acc1 = BankAccount("12345678", "John", "2020-05-23", 50000)

print(acc1.deposit(500))        # Deposit money
print(acc1.withdraw(200))       # Withdraw money
print(acc1.withdraw(2000))      # Withdraw exceeding balance
acc1.check_balance()            # Check balance
acc1.customer_details()         # Show customer details
