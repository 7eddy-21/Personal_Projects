print("Welcome to my computer quiz!")

playing = input("Do you want to play?Yes/No ")

if playing != "Yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CMOS stand for? ")
if answer == "Complementary Metal Oxide Semiconductor":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does DRAM stand for? ")
if answer == "Dynamic Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Who is commonly reffered to as the father of computers? ")
if answer == "Charles Babbage":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ABACUS stand for? ")
if answer == "Abundant Beads Addition Calculation Utility System":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ALU stand for? ")
if answer == "Arithmetical Logical Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("A processor that has 10 cores is an example of which type of processor? ")
if answer == "Deca core processor":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("In data calculation and analysis what does PiB stand for? ")
if answer == "Pebibyte":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which is the part of the computer where all peripherials and components plug into? ")
if answer == "Motherboard":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 10) * 100) + "%")



    


