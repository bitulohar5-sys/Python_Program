import json
import os

# Name of the file where expenses will be stored
FILE_NAME = "expenses.json"


def load_expenses():
    """Load saved expenses from the JSON file."""

    # Check if the file exists
    if not os.path.exists(FILE_NAME):
        return []

    try:
        # Open the file and convert JSON data into Python objects
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    # If the file is empty or contains invalid JSON
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    """Save the current expenses to the JSON file."""

    # Open the file in write mode
    with open(FILE_NAME, "w") as file:
        # Convert Python data into JSON format
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Add a new expense to the expense list."""

    # Get expense details from the user
    name = input("Enter expense name: ")

    try:
        # Convert the entered amount from string to float
        amount = float(input("Enter amount: ₹"))

    except ValueError:
        # Handle invalid amount input
        print("Invalid amount.")
        return

    category = input("Enter category: ")

    # Create a dictionary containing the expense information
    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    # Add the new expense to the list
    expenses.append(expense)

    # Save the updated list to the JSON file
    save_expenses(expenses)

    print("✅ Expense added successfully!")


def view_expenses(expenses):
    """Display all saved expenses."""

    # Check if there are no expenses
    if not expenses:
        print("No expenses found.")
        return

    print("\n------ All Expenses ------")

    # enumerate() gives both the index and the expense
    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. {expense['name']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


def show_total(expenses):
    """Calculate and display the total amount spent."""

    # Add the amount of every expense
    total = sum(expense["amount"] for expense in expenses)

    print(f"\n💰 Total Expenses: ₹{total:.2f}")


def category_summary(expenses):
    """Display total spending for each category."""

    if not expenses:
        print("No expenses found.")
        return

    # Dictionary to store total amount for each category
    summary = {}

    # Go through every expense
    for expense in expenses:
        category = expense["category"]

        # Create the category if it doesn't exist
        if category not in summary:
            summary[category] = 0

        # Add the expense amount to that category
        summary[category] += expense["amount"]

    print("\n------ Category Summary ------")

    # Display each category and its total amount
    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    """Delete an expense using its number."""

    # Display the current expenses first
    view_expenses(expenses)

    if not expenses:
        return

    try:
        # Ask the user which expense should be deleted
        number = int(input("\nEnter expense number to delete: "))

        # Check whether the selected number is valid
        if 1 <= number <= len(expenses):

            # Remove the selected expense
            deleted = expenses.pop(number - 1)

            # Save the updated list
            save_expenses(expenses)

            print(f"🗑️ Deleted: {deleted['name']}")

        else:
            print("Invalid expense number.")

    except ValueError:
        # Handle non-numeric input
        print("Please enter a valid number.")


def main():
    """Main function that runs the Expense Tracker."""

    # Load previously saved expenses
    expenses = load_expenses()

    # Keep showing the menu until the user exits
    while True:

        print("\n============================")
        print("       EXPENSE TRACKER")
        print("============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Category Summary")
        print("5. Delete Expense")
        print("6. Exit")

        # Ask the user to select an option
        choice = input("\nEnter your choice: ")

        # Perform the selected operation
        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_total(expenses)

        elif choice == "4":
            category_summary(expenses)

        elif choice == "5":
            delete_expense(expenses)

        elif choice == "6":
            print("Thank you for using Expense Tracker! 👋")
            break

        else:
            # Handle invalid menu choices
            print("❌ Invalid choice. Please try again.")


# Start the program
# This ensures main() runs only when this file is executed directly
if __name__ == "__main__":
    main()
