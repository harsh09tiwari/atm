import time

print("Please insert Your CARD ")

time.sleep(5)

password = 1234

pin = int(input("Enter your ATM pin: "))

balance = 50000
transaction_history = []  # List to store transaction history

if pin == password:
    while True:
        print("""
            1 == Balance
            2 == Withdraw balance
            3 == Deposit balance
            4 == View transaction history
            5 == Change pin
            6 == Exit
            """)
        try:
            option = int(input("Please enter your choice: "))
        except:
            print("Please enter a valid option")

            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option == 1:
            print(f"Your balance is {balance}")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))

            if withdraw_amount <= balance:
                balance -= withdraw_amount
                transaction_history.append(f"Withdrew {withdraw_amount}. New balance: {balance}")
                print(f"{withdraw_amount} is debited from your account")
            else:
                print("Insufficient balance")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

            print(f"Your current balance is {balance}")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option == 3:
            deposit_amount = int(input("Please enter your deposit amount: "))

            balance += deposit_amount
            transaction_history.append(f"Deposited {deposit_amount}. New balance: {balance}")
            print(f"{deposit_amount} is credited to your account")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

            print(f"Your updated balance is {balance}")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option == 4:
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option == 5:  # Option for changing the pin
            current_pin = int(input("Enter your current pin: "))
            if current_pin == password:
                new_pin = int(input("Enter your new pin: "))
                confirm_pin = int(input("Confirm your new pin: "))
                if new_pin == confirm_pin:
                    password = new_pin
                    print("Your pin has been successfully changed.")
                else:
                    print("New pin and confirmation do not match. Please try again.")
            else:
                print("Incorrect current pin. Please try again.")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option == 6:
            break

else:
    print("Password is incorrect, please try again")
