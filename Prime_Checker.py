while True:
    Number = int(input("Enter the number to be checked: "))
    Checker = 2
    while True:
        if Number % Checker == 0:
            if Checker == Number:
                print(f"{Number} is Prime.")
                break
            else:
                print(f"{Number} is not Prime.")   
                break
        Checker += 1
    Play = input("Do you want to play Yes or No: ").lower().strip()
    if Play != "yes":
        print("Goodbye Thanks for using the program😢.")
        break

#99999989
#100000007