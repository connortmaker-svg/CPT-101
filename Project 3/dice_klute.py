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
                print("NUMBER MUST BE POSITIVE")
        except ValueError:
            print("INVALID INPUT: MUST BE POSITIVE INTEGER")
    return rolls

def increment_roll_count(current_count):
    # increments the number by 1
    return current_count + 1

def stats_dispaly(number, count, total):
    # Calculates the percentage of the number passed through
    if total > 0:
        percentage = (count / total) * 100
    else:
        percentage = 0.0
    print(f"Rolled {number} - {count} times - %{percentage:.2f}")

def write_file(file, num_roll):
    # Writes the data of the rolls to an external .txt file
    print(f"\nWriting results to {file}.....")
    output = open(file, "w")

    for i in range(num_roll):
        result = random.randint(1,6)
        output.write(str(result) + "\n")
    output.close()

def get_roll_count(name, target):
    # Reads the file and counts how many times each "target" (or the number of the die roll) appears
    count = 0 
    try:
        in_file = open(name, "r")
        for line in in_file:
            if int(line.strip()) == target:
                count = increment_roll_count(count)
        in_file.close()
    except FileNotFoundError:
        print("FILE NOT FOUND")
    return count

def main():
    SIDES = 6
    file = "dice_results.txt"

    #Get user input
    total_rolls = get_rolls()

    # Make the File
    write_file(file, total_rolls)

    # Print the Current Rolls to the Terminal
    try:
        with open(file, "r") as dice_file:
            for line in dice_file:
                print(line.strip(), end=" ")
        dice_file.close()
        print("\n\nFinshed rolling the dice")
    except FileNotFoundError:
        print("FILE NOT FOUND")

    print(f"Analying {total_rolls} rolls...\n")

    # Loop for the specific number of sides to the die
    for current_side in range(1, SIDES + 1):
        # Count how many times a specific side appears in the file
        side_count = get_roll_count(file, current_side)
        # pass the count to the display and percent calc function
        stats_dispaly(current_side, side_count, total_rolls)

main()