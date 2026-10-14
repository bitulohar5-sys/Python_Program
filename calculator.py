import math
import csv
from datetime import datetime

# List to store calculation history during the session
history = []


def get_number(prompt_text):
    """Safely get a valid number from the user without crashing."""
    while True:
        try:
            return float(input(prompt_text))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def format_num(n):
    """Format floats cleanly (e.g., 12.0 becomes 12)."""
    if isinstance(n, float) and n.is_integer():
        return int(n)
    return round(n, 6) if isinstance(n, float) else n


def record_history(expression, result):
    """Save the calculation with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history.append({
        "time": timestamp,
        "expression": expression,
        "result": format_num(result)
    })


def show_history():
    """Display all calculations performed in this session."""
    if not history:
        print("\nNo calculations recorded yet.")
        return

    print("\n===== Calculation History =====")
    for idx, item in enumerate(history, start=1):
        print(f"{idx}. [{item['time']}]  {item['expression']} = {item['result']}")


def export_history_csv(filename="calculator_history.csv"):
    """Export the calculation history to a CSV file."""
    if not history:
        print("\nNothing to export! Perform some calculations first.")
        return

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["time", "expression", "result"])
        writer.writeheader()
        writer.writerows(history)
    print(f"\nSaved {len(history)} calculations to '{filename}'!")


def main():
    while True:
        print("\n========= Smart Calculator =========")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Square Root (√)")
        print("8. View History")
        print("9. Export History to CSV")
        print("0. Exit")
        print("====================================")

        choice = input("Enter your choice (0-9): ").strip()

        # Exit the calculator
        if choice == "0":
            print("Thank you for using the calculator!")
            break

        # History & Export options
        if choice == "8":
            show_history()
            continue
        elif choice == "9":
            export_history_csv()
            continue

        # Validate operation choice
        if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice! Please select a valid option (0-9).")
            continue

        # Single-number operation: Square Root
        if choice == "7":
            num = get_number("Enter number: ")
            if num < 0:
                print("Error! Cannot calculate the square root of a negative number.")
            else:
                result = math.sqrt(num)
                expr = f"√({format_num(num)})"
                print(f"Result: {expr} = {format_num(result)}")
                record_history(expr, result)
            continue

        # Two-number operations (Choices 1 to 6)
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == "1":
            result = num1 + num2
            symbol = "+"
        elif choice == "2":
            result = num1 - num2
            symbol = "-"
        elif choice == "3":
            result = num1 * num2
            symbol = "*"
        elif choice == "4":
            if num2 == 0:
                print("Error! Cannot divide by zero.")
                continue
            result = num1 / num2
            symbol = "/"
        elif choice == "5":
            if num2 == 0:
                print("Error! Cannot find modulus with zero.")
                continue
            result = num1 % num2
            symbol = "%"
        elif choice == "6":
            result = num1 ** num2
            symbol = "**"

        # Display and log the result
        expr = f"{format_num(num1)} {symbol} {format_num(num2)}"
        print(f"Result: {expr} = {format_num(result)}")
        record_history(expr, result)


if __name__ == "__main__":
    main()