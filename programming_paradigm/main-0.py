import sys
import json
from bank_account import BankAccount

BALANCE_FILE = "account_balance.json"

def load_balance():
    try:
        with open(BALANCE_FILE, "r") as f:
            return json.load(f).get("balance", 100)  # Default to 100 if file missing
    except (FileNotFoundError, json.JSONDecodeError):
        return 100  # Default balance

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        json.dump({"balance": balance}, f)

def main():
    account = BankAccount(load_balance())

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")

    elif command == "display":
        account.display_balance()

    else:
        print("Invalid command.")

    # Save balance after each operation
    save_balance(account.account_balance)

if __name__ == "__main__":
    main()
