import json
import os

FILE_NAME = "expenses.json"


# Load expenses from JSON file
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save expenses to JSON file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


# Add a new expense
def add_expense(expenses):
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")


# Display all expenses
def view_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return

    print("\n------ Expenses ------")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['name']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['category']}"
        )


# Calculate total expenses
def total_expenses(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")


# Show expenses by category
def category_summary(expenses):
    if not expenses:
        print("No expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        summary[category] = summary.get(category, 0) + expense["amount"]

    print("\n------ Category Summary ------")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


# Delete an expense
def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses(expenses)

            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():
    expenses = load_expenses()

    while True:
        print("\n========================")
        print("      EXPENSE TRACKER")
        print("========================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expenses(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


# Start the program
if __name__ == "__main__":
    main()