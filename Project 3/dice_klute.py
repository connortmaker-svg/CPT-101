# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 3
# Dice Rolling Simulation
# ----------------------------------

import random # For Random Funtionality

def get_rolls():
    # Handles the initial user input into the program and validates it
    rolls = 0
    is_valid = False

    # Loop to Check valid input
    while is_valid == False:
        try:
            rolls = int(input("How many times to roll the die?  "))
            
            if rolls > 0:
                is_valid = True
            else:
                print("Plase Enter a Valid number Greater than 0")
        except ValueError:
            print("INVALID INPUT")
    return rolls

def write_file(file, num_roll):

def read_file(file, total_roll):

def main():

main()