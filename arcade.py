import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit Ksh? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be greater than 0.")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line(1-" + str(MAX_BET) + ")? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between Ksh {MIN_BET} - Ksh {MAX_BET}.")
        else:
            print("Please enter a number")
    return amount

def run_code(): 
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money to bet that amount, your current balance is: Ksh {balance}")
        else:
            break    

    print(f"You are betting Ksh {bet} on {lines} lines. Total bet is equal to Ksh {total_bet}")
        
run_code()