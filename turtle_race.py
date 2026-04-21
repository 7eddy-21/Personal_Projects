import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'teal', 'cyan', 'pink', 'orange', 'yellow', 'purple', 'black']

def get_no_racers():
    racers = 0 
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please type a numeric value from 2 - 10")
            continue
        
        if 2 <= racers <= 10:
            return racers  
        else:
            print("number not in range 2 - 10.Please Try again!")

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 5)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i +1) * spacingx, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return  turtles
        
def init_turle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race .Ult")

racers = get_no_racers()
init_turle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The {winner} Turtle won!")
time.sleep(5)