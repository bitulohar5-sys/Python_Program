# Simple Calculator Program

# Keep running the calculator until the user chooses to exit
while True:

    print("\n===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-7): ")

    # Exit the calculator
    if choice == "7":
        print("Thank you for using the calculator!")
        break

    # Check whether the choice is valid
    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice! Please try again.")
        continue

    # Get two numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        # Check for division by zero
        if num2 == 0:
            print("Error! Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    elif choice == "5":
        # Check for modulus by zero
        if num2 == 0:
            print("Error! Cannot find modulus with zero.")
        else:
            result = num1 % num2
            print("Result:", result)

    elif choice == "6":
        result = num1 ** num2
        print("Result:", result)