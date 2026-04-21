from playsound3 import playsound
import time

Clear_Terminal = "\033[2J"
Clear_And_Return = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(Clear_Terminal)

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{Clear_And_Return}Alarm will sound in {minutes_left:02d}:{seconds_left:02d}")
    playsound("Ransom.m4a")

minutes = int(input("Enter number of minutes before alarm. "))
seconds = int(input("Enter number of seconds before alarm. "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)