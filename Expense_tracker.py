import json
import os
from datetime import datetime

FILE_NAME = "transactions.json"


# -----------------------------
# Load Transactions
# -----------------------------
def load_transactions():
    """Load saved transactions from JSON file."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


# -----------------------------
# Save Transactions
# -----------------------------
def save_transactions(transactions):
    """Save transactions to JSON file."""

    with open(FILE_NAME, "w") as file:
        json.dump(transactions, file, indent=4)


# -----------------------------
# Add Income
# -----------------------------
def add_income(transactions):
    """Add a new income transaction."""

    source = input("Enter income source: ")

    try:
        amount = float(input("Enter income amount: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

    except ValueError:
        print("❌ Invalid amount.")
        return

    date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today's date: "
    )

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format.")
        return

    income = {
        "type": "income",
        "name": source,
        "amount": amount,
        "category": "Income",
        "date": date
    }

    transactions.append(income)
    save_transactions(transactions)

    print("✅ Income added successfully!")


# -----------------------------
# Add Expense
# -----------------------------
def add_expense(transactions):
    """Add a new expense transaction."""

    name = input("Enter expense name: ")

    try:
        amount = float(input("Enter expense amount: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

    except ValueError:
        print("❌ Invalid amount.")
        return

    category = input("Enter category: ")

    date = input(
        "Enter date (YYYY-MM-DD) or press Enter for today's date: "
    )

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format.")
        return

    expense = {
        "type": "expense",
        "name": name,
        "amount": amount,
        "category": category,
        "date": date
    }

    transactions.append(expense)
    save_transactions(transactions)

    print("✅ Expense added successfully!")


# -----------------------------
# View Transactions
# -----------------------------
def view_transactions(transactions):
    """Display all transactions."""

    if not transactions:
        print("\n❌ No transactions found.")
        return

    print("\n========== TRANSACTIONS ==========")

    for index, transaction in enumerate(transactions, start=1):

        transaction_type = transaction["type"].upper()

        print(
            f"{index}. "
            f"{transaction['date']} | "
            f"{transaction_type} | "
            f"{transaction['name']} | "
            f"₹{transaction['amount']:.2f} | "
            f"{transaction['category']}"
        )


# -----------------------------
# Total Income
# -----------------------------
def total_income(transactions):
    """Calculate total income."""

    income = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "income"
    )

    return income


# -----------------------------
# Total Expenses
# -----------------------------
def total_expenses(transactions):
    """Calculate total expenses."""

    expenses = sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense"
    )

    return expenses


# -----------------------------
# Savings
# -----------------------------
def calculate_savings(transactions):
    """Calculate savings."""

    income = total_income(transactions)
    expenses = total_expenses(transactions)

    return income - expenses


# -----------------------------
# Category-wise Spending
# -----------------------------
def category_wise_spending(transactions):
    """Calculate expenses for each category."""

    if not transactions:
        print("\n❌ No transactions found.")
        return

    categories = {}

    for transaction in transactions:

        if transaction["type"] == "expense":

            category = transaction["category"]

            if category not in categories:
                categories[category] = 0

            categories[category] += transaction["amount"]

    if not categories:
        print("\n❌ No expenses found.")
        return

    print("\n========== CATEGORY-WISE SPENDING ==========")

    for category, amount in categories.items():
        print(f"{category:<20} ₹{amount:.2f}")


# -----------------------------
# Monthly Spending
# -----------------------------
def monthly_spending(transactions):
    """Calculate expenses month-wise."""

    if not transactions:
        print("\n❌ No transactions found.")
        return

    monthly = {}

    for transaction in transactions:

        if transaction["type"] == "expense":

            month = transaction["date"][:7]

            if month not in monthly:
                monthly[month] = 0

            monthly[month] += transaction["amount"]

    if not monthly:
        print("\n❌ No expenses found.")
        return

    print("\n========== MONTHLY SPENDING ==========")

    for month, amount in sorted(monthly.items()):
        print(f"{month} : ₹{amount:.2f}")


# -----------------------------
# Financial Dashboard
# -----------------------------
def dashboard(transactions):
    """Display complete financial summary."""

    income = total_income(transactions)
    expenses = total_expenses(transactions)
    savings = calculate_savings(transactions)

    print("\n======================================")
    print("          FINANCIAL DASHBOARD")
    print("======================================")

    print(f"💰 Total Income     : ₹{income:.2f}")
    print(f"💸 Total Expenses   : ₹{expenses:.2f}")
    print(f"💵 Total Savings    : ₹{savings:.2f}")

    if income > 0:
        saving_percentage = (savings / income) * 100
        print(f"📊 Saving Rate      : {saving_percentage:.2f}%")

    print("======================================")


# -----------------------------
# Delete Transaction
# -----------------------------
def delete_transaction(transactions):
    """Delete a transaction."""

    view_transactions(transactions)

    if not transactions:
        return

    try:
        number = int(input("\nEnter transaction number to delete: "))

        if 1 <= number <= len(transactions):

            deleted = transactions.pop(number - 1)

            save_transactions(transactions)

            print(
                f"🗑️ Deleted: "
                f"{deleted['name']} - "
                f"₹{deleted['amount']:.2f}"
            )

        else:
            print("❌ Invalid transaction number.")

    except ValueError:
        print("❌ Please enter a valid number.")


# -----------------------------
# Main Menu
# -----------------------------
def main():

    transactions = load_transactions()

    while True:

        print("\n======================================")
        print("       SMART EXPENSE TRACKER")
        print("======================================")

        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Transactions")
        print("4. Financial Dashboard")
        print("5. Category-wise Spending")
        print("6. Monthly Spending")
        print("7. Delete Transaction")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_income(transactions)

        elif choice == "2":
            add_expense(transactions)

        elif choice == "3":
            view_transactions(transactions)

        elif choice == "4":
            dashboard(transactions)

        elif choice == "5":
            category_wise_spending(transactions)

        elif choice == "6":
            monthly_spending(transactions)

        elif choice == "7":
            delete_transaction(transactions)

        elif choice == "8":
            print("\nThank you for using Smart Expense Tracker! 👋")
            break

        else:
            print("❌ Invalid choice. Please try again.")


# -----------------------------
# Start Program
# -----------------------------
if __name__ == "__main__":
    main()