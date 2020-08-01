# Import modules
import math
import random

# Print welcome message
print ("Welcome to Battleship!")

# Define function
def battleship():
    randomLoc = math.floor(random.randint(0,4))
    location1 = randomLoc
    location2 = location1 + 1
    location3 = location2 + 1
    guess = 0
    hits = 0
    guesses = 0
    isSunk = False

    # Main loop
    while isSunk == False:
        guess = int(input("Ready, aim, fire! Enter a number 0-6:"))
        if guess < 0 or guess > 6 :
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
                input()

# Call function
battleship()
