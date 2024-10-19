import pickle
import os

Dollars = 1
Dollars_in_hand = 1

def load_handmoney():
    global Dollars_in_hand
    if os.path.exists("moneyinhand"):
        with open("moneyinhand", "rb") as file:
            Dollars_in_hand = pickle.load(file)

def load_bankmoney():
    global Dollars
    if os.path.exists("moneyinbank"):
        with open("moneyinbank", "rb") as file:
            Dollars = pickle.load(file)


def save_handmoney():
    global Dollars_in_hand
    with open("moneyinhand", "wb") as file:
        pickle.dump(Dollars_in_hand, file)

def save_bankmoney():
    global Dollars_in_hand
    with open("moneyinbank", "wb") as file:
        pickle.dump(Dollars, file)

def balance():
    global Dollars
    print()
    print(f"| Your current balance is: ${round(Dollars, 2)}! |")
    print()
    Options2()

def withdraw():
    global Dollars_in_hand
    global Dollars
    print()
    f = input("| How many dollars would you like to withdraw? (Type 0 to go back): $")
    print()
    
    if f == "0":
        Options2()
    else:
        try:
            f = float(f)
            if f > Dollars:
                print()
                o = input("| Insufficient funds! Would you like to retry? (Y/N/B for balance): ")
                print()
                if o.upper() == "Y":
                    withdraw()
                elif o.upper() == "N":
                    Options2()
                elif o.upper() == "B":
                    balance()
            elif f <= Dollars:
                Dollars_in_hand += f
                Dollars -= f
                print()
                k = input("| Withdrawal succesful! Would you like to try again? (Y/N): ")
                print()
                if k.upper() == "Y":
                    withdraw()
                elif k.upper() == "N":
                    Options2()
        except ValueError:
            print()
            print("| That is not a valid number. |")
            print()
            withdraw()

def deposit():
    global Dollars
    global Dollars_in_hand
    print()
    y = input("| How many dollars would you like to deposit? (Type 0 to go back): $")
    print()
    
    if y == "0":
        Options2()
    else:
        try:
            y = float(y)
            if y > Dollars_in_hand:
                print()
                g = input("| Insufficient funds! Would you like to try again? (Y/N/Type B for balance): ")
                print()
                if g.upper() == "Y":
                    deposit()
                elif g.upper() == "N":
                    Options2()
                elif g.upper() == "B":
                    balance()
            elif y <= Dollars_in_hand:
                Dollars_in_hand -= y
                Dollars += y
                print()
                h = input("| Deposit succesful! Would you like to try again? (Y/N): ")
                print()
                if h.upper() == "Y":
                    deposit()
                elif h.upper() == "N":
                    Options2()
        except ValueError:
            print()
            print("| That is not a valid number. |")
            print()
            deposit()

def Options():
    global Dollars_in_hand
    print()
    print("|       Welcome to the Bank!        |")
    print("| Please pick a choice below! (0-4) |")
    print("| 0. Exit                           |")
    print("| 1. Balance in bank                |")
    print("| 2. Balance in hands               |")
    print("| 3. Deposit                        |")
    print("| 4. Withdraw                       |")
    user_input = input("| ")
    print()

    if user_input == "1":
        balance()
    elif user_input == "2":
        print()
        print(f"| Your current amount of money in hands are: ${round(Dollars_in_hand, 2)}! |")
        print()
        Options2()
    elif user_input == "3":
        deposit()
    elif user_input == "4":
        withdraw()
    elif user_input == "0":
        save_bankmoney()
        save_handmoney()
        exit()
    else:
        print()
        print("| That is not a valid choice. |")
        print()
        Options2()

def Options2():
    global Dollars_in_hand
    print()
    print("| Please pick a choice below! (0-4) |")
    print("| 0. Exit                           |")
    print("| 1. Balance in bank                |")
    print("| 2. Balance in hands               |")
    print("| 3. Deposit                        |")
    print("| 4. Withdraw                       |")
    user_input = input("| ")
    print()

    if user_input == "1":
        balance()
    elif user_input == "2":
        print()
        print(f"| Your current amount of money in hands are: ${round(Dollars_in_hand, 2)}! |")
        print()
        Options2()
    elif user_input == "3":
        deposit()
    elif user_input == "4":
        withdraw()
    elif user_input == "0":
        save_bankmoney()
        save_handmoney()
        exit()
    else:
        print()
        print("| That is not a valid choice. |")
        print()
        Options2()

load_handmoney()
load_bankmoney()
Options()