# Import modules
import math
import random

print ("Welcome to Battleship!")

# Define function
def battleship():
    randomLoc = math.floor(random.randint(0,8))
    location1 = randomLoc
    location2 = location1 + 1
    location3 = location2 + 1
    guess = 0
    hits = 0
    guesses = 0
    isSunk = False

    # Main loop
    while isSunk == False:
        guess = int(input("READY, AIM, FIRE! Enter a number 0-10:"))
        if guess < 0 or guess > 10 :
            print ("Please enter a valid cell number!")
        else: 
            guesses = guesses + 1
            if guess == location1 or guess == location2 or guess == location3:
                hits = hits + 1
                print ("HIT!")
            elif guess != location1 or location2 or location3:
                print ("MISS")
            if hits == 3:
                isSunk = True
                print ("You sank my battleship!")

# Call function
battleship()

playAgain = 0

while playAgain != 2:
    print("Play again?")
    playAgain = ["1. Press 1 to play again.", "2. Press 2 to exit."]
    for item in playAgain:
        print(item)
    playAgain = int(input())
    if playAgain == 1:
        battleship()
    elif playAgain == 2:
        exit
