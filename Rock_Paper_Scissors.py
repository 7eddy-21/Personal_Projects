import random

user_wins = 0
computer_wins = 0
options = ["ROCK", "PAPER", "SCISSORS"]
options[0]

while True:
    user_input = input("Type ROCK, PAPER, SCISSORS or QUIT: ").upper()
    if user_input == "QUIT":
        break

    if user_input not in options:
        print("Please type a valid answer.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It is a draw!")
    elif user_input == "ROCK" and computer_pick == "SCISSORS" or user_input == "PAPER" and computer_pick == "ROCK" or user_input == "SCISSORS" and computer_pick == "PAPER":
            print("You won!")
            user_wins += 1
    else:
        
        print("You lost!")
        computer_wins += 1
print(f"You won {user_wins} times.")
print(f"Computer won {computer_wins} times.")
print("End of the game gcoodbye")        








