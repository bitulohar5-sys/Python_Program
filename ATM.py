# ==============================
# Simple ATM Simulation in Python
# ==============================

def atm():
    # User details
    user_pin = "1234"
    balance = 10000
    transactions = []

    print("================================")
    print("      WELCOME TO PYTHON ATM")
    print("================================")

    # ------------------------------
    # PIN Verification
    # ------------------------------
    attempts = 3

    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")

        if entered_pin == user_pin:
            print("\nPIN accepted successfully!")
            break
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempt(s) left.\n")

    if attempts == 0:
        print("Too many incorrect attempts.")
        print("Your card has been blocked.")
        return

    # ------------------------------
    # Main ATM Menu
    # ------------------------------
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Exit")
        print("==============================")

        choice = input("Choose an option (1-6): ")

        # --------------------------
        # Check Balance
        # --------------------------
        if choice == "1":
            print(f"\nYour current balance is: ₹{balance:.2f}")

        # --------------------------
        # Deposit Money
        # --------------------------
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: ₹"))

                if amount > 0:
                    balance += amount
                    transactions.append(f"Deposited: ₹{amount:.2f}")
                    print(f"₹{amount:.2f} deposited successfully.")
                    print(f"New balance: ₹{balance:.2f}")
                else:
                    print("Invalid amount. Enter a positive amount.")

            except ValueError:
                print("Please enter a valid number.")

        # --------------------------
        # Withdraw Money
        # --------------------------
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: ₹"))

                if amount <= 0:
                    print("Invalid amount. Enter a positive amount.")

                elif amount > balance:
                    print("Insufficient balance.")

                else:
                    balance -= amount
                    transactions.append(f"Withdrawn: ₹{amount:.2f}")
                    print(f"₹{amount:.2f} withdrawn successfully.")
                    print(f"Remaining balance: ₹{balance:.2f}")

            except ValueError:
                print("Please enter a valid number.")

        # --------------------------
        # Mini Statement
        # --------------------------
        elif choice == "4":
            print("\n======= MINI STATEMENT =======")

            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                for transaction in transactions:
                    print(transaction)

            print(f"Current Balance: ₹{balance:.2f}")
            print("==============================")

        # --------------------------
        # Change PIN
        # --------------------------
        elif choice == "5":
            current_pin = input("Enter your current PIN: ")

            if current_pin == user_pin:
                new_pin = input("Enter your new 4-digit PIN: ")

                if len(new_pin) == 4 and new_pin.isdigit():
                    confirm_pin = input("Confirm your new PIN: ")

                    if new_pin == confirm_pin:
                        user_pin = new_pin
                        print("PIN changed successfully.")
                    else:
                        print("PINs do not match.")
                else:
                    print("PIN must contain exactly 4 digits.")

            else:
                print("Incorrect current PIN.")

        # --------------------------
        # Exit
        # --------------------------
        elif choice == "6":
            print("\nThank you for using Python ATM!")
            print("Have a great day. Goodbye!")
            break

        # --------------------------
        # Invalid Choice
        # --------------------------
        else:
            print("Invalid option. Please choose between 1 and 6.")


# ==============================
# Run the ATM Program
# ==============================

atm()