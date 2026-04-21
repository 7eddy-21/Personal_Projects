from playsound3 import playsound
def year_collection():
    while True:
        try:
            year = int(input("Enter year to be checked: "))
            if year % 4 == 0 and year % 100 != 0:
                print(f"{year} is a leap year.")
                playsound("Leap.m4a")
                break
            else:
                print(f"{year} is not a leap year.")
                break
        except:
            print("ERROR❌❌.Enter a whole number for the program to work")

def play_again():
    while True:
        chance = input("Do you want to test another year, Yes or No: ").lower().strip()
        if chance == "yes":
            year_collection()
        elif chance == "no":
            print("Thanks for using my program👋.😎😎")
            break
        else:
            print("The valid choices are yes or no.")
            break
    
def main():
    year_collection()
    play_again()

main()
