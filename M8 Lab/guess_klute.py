# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M8 Lab - Loop Basics
# Guess the Number
# ----------------------------------

import random # Ability to utilize random functionality in a program

print("Play a game!\n")

# Create the random number
number = random.randint(1,10)
# The Users guess count to track to give them x amount of attempts
guess_count = 1

# The Users input guess
guess = int(input("What is a number between 1 and 10?  "))

# the Constant loop checkling if the user guess is not the number, and repeating
while guess != number:
    print(f"{guess} is not the right answer. Try again" )
    guess = int(input("What is your new guess: "))
    guess_count += 1 

print(f"FINALLY thought that would take forever. I guess only {guess_count} attempts to find the number {number}")