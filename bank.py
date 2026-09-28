import json
class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        self.transactions = []
    def deposit (self,amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount}. New balance: {self.balance}")
        self.transactions.append(f"Deposit: +{amount}")
    def withdraw(self ,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
            self.transactions.append(f"Withdrawal: -{amount}")
    def show_history(self):
        print(f"History for {self.owner}:")
        for item in self.transactions:
            print(item)
    def to_dict(self):
        return {
            "owner": self.owner ,
            "balance": self.balance ,
            "transactions": self.transactions
        }
def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        return[]
    accounts = []
    for item in data:
        acc = Account(item["owner"], item["balance"])
        acc.transactions = item["transactions"]
        accounts.append(acc)
    return accounts
def save_accounts(accounts):
    data = []
    for acc in accounts:
        data.append(acc.to_dict())
    with open("accounts.json", "w") as file:
        json.dump(data, file, indent=4)
def find_account(accounts, name):
    for acc in accounts:
        if acc.owner.lower() == name.lower():
            return acc
    return None
def get_amount(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value <= 0:
            print("Amount must be greater than zero.")
            continue
        return value
accounts = load_accounts()
while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Show history")
    print("6. Quit")
    choice = input("choose an option: ")
    if choice == "1":
        name = input("Owner name: ")
        opening = get_amount("Opening balance: ")
        accounts.append(Account(name, opening))
        save_accounts(accounts)
        print("Account created.")
    elif choice in ("2","3","4","5"):
        name = input("Owner name: ")
        acc = find_account(accounts, name)
        if acc is None:
            print("Account not found")
        elif choice == "2":
            acc.deposit(get_amount("Amount: "))
            save_accounts(accounts)
        elif choice == "3":
            acc.withdraw(get_amount("Amount: "))
            save_accounts(accounts)
        elif choice == "4":
            print(f"{acc.owner}'s balance: {acc.balance}")
        elif choice == "5":
            acc.show_history()
    elif choice == "6":
        print("Goodbye.")
        break
    else:
        print("Invalid option.")

