"""Write a Python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal
"""
class BankAccount:
    def __init__(self, username, password, name, address, phone_number, balance=0):
        self.username = username
        self.password = password
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.balance = balance

    def login(self, password_entered):
        return password_entered == self.password

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Amount {amount} deposited successfully. Current balance: {self.balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Amount {amount} withdrawn successfully. Current balance: {self.balance}")
        else:
            print("Insufficient balance")

def create_account():
    username = input("Enter username: ")
    password = input("Enter password: ")
    name = input("Enter name: ")
    address = input("Enter address: ")
    phone_number = input("Enter phone number: ")
    return BankAccount(username, password, name, address, phone_number)

accounts = {}

while True:
    print("\nWelcome to the banking system")
    print("1. Create account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        new_account = create_account()
        accounts[new_account.username] = new_account
        print("Account created successfully")
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in accounts:
            if accounts[username].login(password):
                current_account = accounts[username]
                print("Login successful")
                while True:
                    print("\n1. Deposit")
                    print("2. Withdraw")
                    print("3. Logout")
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        current_account.deposit(amount)
                    elif sub_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        current_account.withdraw(amount)
                    elif sub_choice == '3':
                        break
                    else:
                        print("Invalid choice. Please try again")
            else:
                print("Invalid password")
        else:
            print("Account not found")
    elif choice == '3':
        print("Thank you for using our banking system")
        break
    else:
        print("Invalid choice. Please try again")

