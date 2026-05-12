# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Final Project
# Adventure Quest
# ----------------------------------

import random # For Random Functionality

def display_menu():
    # Prints out the Menu for the User to Interact with.
    print("1 | Explore your Surroundings")
    print("2 | Have an Encounter")
    print("3 | View Inventory and Player Stats")
    print("4 | Fight the Dungeon Boss")
    print("5 | Exit the Game")

def menu_select():
    # Initalization Variables
    v_input = False
    option = 0
    while not v_input:
        try:
            # Inital User Input
            option = int(input("Enter a Menua Option between 1 and 5:"))
            display_menu()
            # Range Validation
            if option >=1 and option <=5:
                v_input = True
            else:
                print("Must be between 1 and 5")
        # Error Handling
        except ValueError:
            print("Must be a valid integer")
    # Output the users Option
    return option

def explore_scene(health, gold):
    # Scenario 1
    # Scenario 2
    # Scenario 3
    # Scenario 4
    # Scenario 5
    # Scenario 6
    # Scenario 7 
    # Scenario 8
    # Scenario 9
    # Scenario 10
    return health, gold

def encounters(health, gold, inventory):
    # Encounter 1
    # Encounter 2
    # Encounter 3
    # Encounter 4
    # Encounter 5
    # Encounter 6
    # Encounter 7
    return health, gold, inventory

def display_stats(health, gold, inventory):
    return health, gold, inventory

def display_inventory(inventory):
    return list

def final_boss_option(health, gold, inventory):
    return 1

def main():
    gold = 20
    health = 10
    inventory = []

    game_over = False

    if game_over == False:
        # Do everything
        return 1
    else:
        exit():

main()