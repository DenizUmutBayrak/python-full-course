# Python Banking Program

def show_balance():
    print(f"Your balance is ${balance:.2f}")
    pass

def deposit():
    amount = float(input("Enter your deposit amount: "))

    if amount < 0:
        print("That isn't a valid amount. ")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn: "))

    if amount < 0:
        print("That isn't a valid amount. ")
        return 0
    else:
        return amount

balance = 0
is_running = True

while is_running :
    print()
    print("Banking Program")
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")


    choice = input("Enter your choice: ( 1 - 4 ): ")
    print()

    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposit()
    elif choice == "3":
        balance -= withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("Invalid Choice")

print("Thank You, Have a nice day!")

