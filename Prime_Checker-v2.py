import math
while True:
    Number = int(input("Enter the number to be checked😊. "))
    if Number < 2:
        print(f"{Number} is not Prime")
    else:
        limit = math.isqrt(Number)
        Checker = 2
        Is_Prime = True
        while Checker <=limit:
            if Number % Checker == 0:
                Is_Prime = False
                break
            Checker += 1
        if Is_Prime:
            print(f"{Number} is Prime.")
        else:
            print(f"{Number} is not Prime.")
    Play = input("Do you want to play agin Yes or No: ").lower().strip()
    if Play != "yes":
        break