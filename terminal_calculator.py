def addition():
    while True:
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            answer = number_1 + number_2
            print (answer)
            break
        except:
            print("ERROR❌❌.Enter numerical values for the code to work")

def subtraction():
     while True:
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            answer = number_1 - number_2
            print (answer)
            break
        except:
            print("ERROR❌❌.Enter numerical values for the code to work")

def multiplication():
     while True:
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            answer = number_1 * number_2
            print (answer)
            break
        except:
            print("ERROR❌❌.Enter numerical values for the code to work")

def division():
     while True:
        try:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            answer = number_1 / number_2
            print (answer)
            break
        except:
            print("ERROR❌❌.Enter numerical values for the code to work")

def choose_operation():
    while True:
        operation_type = input("Choose the type of operation to be perfomed Mul,Div,Sub,Add: ").lower().strip()
        if operation_type == "mul":
            multiplication()
            break
        elif operation_type == "div":
            division()
            break
        elif operation_type == "sub":
            subtraction()
        elif operation_type == "add":
            addition()
            break
        else:
            print("ERROR❌❌.Enter correct arithmetical operation.")

def play_again():
    while True:
        chance = input("Do you want to calculate again, Yes or No: ").lower().strip()
        if chance == "yes":
            choose_operation()
        elif chance == "no":
            print("Thanks for using my program👋.😎😎")
            break
        else:
            print("The valid choices are yes or no.")
            break
    
def main():
    choose_operation()
    play_again()

main()