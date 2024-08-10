import time

print("Please insert Your CARD ")

time.sleep(5)

password=1234

pin=int(input("enter your atm pin "))

balance =50000
transaction_history=[]

if pin==password:
    while True:
    
        print("""
            1==balance
            2==withdraw balance
            3=deposit balance
            4==pin change
            5==view transaction history
            6==exit
            """
            )
        try:
            option=int(input("Please enter your choice "))
        except:
            print("Please enter valid option ")

            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option==1:
            print(f"Your balance is {balance}")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")
        if option==2:
            withdraw_amount=int(input("Please enter withdraw_amount "))
            if withdraw_amount<=balance:
                balance=balance-withdraw_amount
                transaction_history.append(f"withdraw{withdraw_amount}. New balance: {balance}")
                print(f"{withdraw_amount} is debited from your account")

            else:
                print("Insufficient balance")    

            
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

            print(f"your current balance is {balance}")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option==3:
            deposit_amount=int(input("Please enter your deposit amount "))

            balance=balance+deposit_amount
            transaction_history.append(f"Deposited{deposit_amount}. New balance: {balance}")

            print(f"{deposit_amount} is credited to your account")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

            print(f"your updated balance is {balance}")
            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option==4:
            new_pin=int(input("please enter your new pin "))
            confirm_pin=int(input("confirm your new pin "))
            if new_pin==confirm_pin:
                password= new_pin
                print("pin in changed successfully")
            
            else:
                print("new pin and confirmation does not match")
                print("Please try again")


            print("===============================================================")
            print("===============================================================")
            print("===============================================================")

        if option==5:
            if transaction_history:
                print("Transaction history")
                for transaction in transaction_history:
                    print(transaction)


            else:
                print("No transaction history")
        

        print("===============================================================")
        print("===============================================================")
        print("===============================================================")
        
        if option==6:
            break


else:
    print("Passoword is incorrect please try again")