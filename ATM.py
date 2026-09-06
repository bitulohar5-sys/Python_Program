# Simple ATM Simulation in Python

def atm():
    # Predefined user credentials
    user_pin = "1234"
    balance = 100000000000 # initial balance

    print("Welcome to Python ATM!")
    attempts = 3

    # PIN verification
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == user_pin:
            print("PIN accepted.\n")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempt(s) left.\n")


    if attempts == 0:
        print("Too many incorrect attempts. Card blocked.")
        return

    # Main menu loop
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"\nYour current balance is: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "4":
            print("Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 4.")

# Run the ATM program
atm()
