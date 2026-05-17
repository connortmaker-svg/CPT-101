# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Final Project
# Adventure Quest
# ----------------------------------

import random # For Random Functionality
import sys # For dynamically closing the program

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
    print("\nVenturing deeper into the dragon's territory you look around to see what you can find")

    # Random Selection for scenarios
    scenario = random.randint(1,6)

    if scenario == 1:
        # Each Scenario follows the same layout of code
        # Found gold
        print("You stumble onto a pile of ungruard gold near a drake's nest!")

        # Random Selection
        coins = random.randint(10,40)
        gold += coins
        print(f"You quickly pocket {coins} gold coins")
        print(f"You now have {gold} coins")
    
    elif scenario == 2:
        # Lose Health
        print("A wyvern swoops down and grazes you with its fiery breath")
        health_lost = random.randint(1, 3)
        health -= health_lost
        print(f"You suffered a burn and lost {health_lost} health point(s).")
        print(f"You now have {health} health points.")
        
    elif scenario == 3:
        # Gain Health
        print("You discover a glowing, magical spring blessed by Elves.")
        health_gained = random.randint(2, 5)
        health += health_gained
        print(f"Drinking the water restores {health_gained} health point(s).")
        print(f"You now have {health} health points.")
        
    elif scenario == 4:
        # Lose Gold
        print("A sneaky forest goblin cuts your coin purse while you were watching the skies")
        coins_lost = random.randint(5, 15)
        gold -= coins_lost
        print(f"The goblin made off with {coins_lost} gold coins.")
        print(f"You now have {gold} gold coins.")
    
    elif scenario == 5:
        # Lose Health; Gain Gold
        print("You fight off a group of skeletons guarding an ancient chest")
        health_lost = random.randint(1, 2)
        coins = random.randint(15, 30)
        health -= health_lost
        gold += coins
        print(f"You took {health_lost} damage in the fight, but found {coins} gold coins in the chest.")
        print(f"You now have {health} health points and {gold} gold coins.")
        
    elif scenario == 6:
        # Lose Gold; Gain health
        print("You meet a wandering alchemist who forces you to buy a dragon-blood elixir.")
        coins_lost = random.randint(5, 10)
        health_gained = random.randint(1, 4)
        gold -= coins_lost
        health += health_gained
        print(f"You paid {coins_lost} gold coins, but the elixir gave you {health_gained} health point(s).")
        print(f"You now have {health} health points and {gold} gold coins.")
    
    return health, gold

def encounters(health, gold, inventory):
    print("\nYou look around and spot someone...... or something..... approaching...")

    # Random select of encounters
    encounter = random.randint(1,5)
    # Logic Block for different encounters:
    if encounter == 1:
        # Gain an Item
        print("An old wizard approaches. He ands you a Dragon-bone Wand")
        # Add Item to inventory:
        inventory.append("Dragon-Bone Wand")
        # Show the User their current inventory
        print("Your Invnetory:")
        print_list(inventory)
    
    elif encounter == 2:
        # Gain two Items
        print("You find the remains of a fallen dragon-slayer. You respectfully take their gear.")
        inventory.append("Steel Shield")
        inventory.append("Vial of Dragon Tears")
        print("Your inventory:")
        print_list(inventory)
        
    elif encounter == 3:
        # Lose an Item
        print("A swift Kobold darts out of the shadows and tries to snatch your gear!")
        # Checks if you have any items to steal
        if len(inventory) > 0:
            stolen_item = inventory.pop(0)
            print(f"Oh no! The Kobold ran away with your {stolen_item}.")
            print("Your inventory:")
            print_list(inventory)
        else:
            print("Your inventory is already empty. The Kobold hisses and runs away.")
    
    elif encounter == 4:
        # Gain an Item; lose gold
        print("A Dwarven blacksmith offers to sell you a Mithril Dagger for 15 gold.")
        inventory.append("Mithril Dagger")
        gold -= 15
        print("Your inventory:")
        print_list(inventory)
        print(f"You paid the blacksmith and now have {gold} gold coins.")
        
    elif encounter == 5:
        # Zero Items to be Collected
        print("You carefully sneak past a sleeping Red Dragon. It's best not to wake it.")
        print("You quietly slip away without gaining or losing anything.")
    
    return health, gold, inventory

def display_stats(health, gold, inventory):
    # Takes in the Current Health, Gold, and inventory list of the player then will print it out. 
    print("Current Player Stats:")
    print(f"Gold Coins: {gold}")
    print(f"Health Points: {health}")
    print(f"Number of items: {len(inventory)}")
    print("\nYour Current Inventory:")
    print_list(inventory)

def print_list(inventory):
    # Index through every item in the list and print each individual item
    for item in inventory:
        print(item)

def final_boss_option(health, gold, inventory):
    num_items = len(inventory)
    if health > 0 and gold >= 100 and num_items >= 4:
        final_boss()
    else:
        print("Come back when you are actually ready")

def final_boss(health, gold, inventory):
    num_items = len(inventory)
    print("\nYou Have chosen to face the 7 Headed Dragon!")
    # Logic Check if player has needed stats to face the boss
    if health > 0 and gold >= 100 and num_items >= 4:
        print("You've arrived prepared to deaft the 7 Headed Dragon and Take it Down with ease!!")
        return True # Returning True means game_over becomes True
    else:
        print("You are not ready!")
        # Let the user know exactly what they are missing
        if gold < 100:
            print(f"You need {100 - gold} more gold coins.")
        if health <= 0:
            print("Your health is too low! You need to be above 0.")
        if num_items < 4:
            print(f"You need {4 - num_items} more item(s).")

    return False

def exit(health, gold, inventory):
    print("\nYou gave up and ran away")
    # Show Player Stats
    display_stats(health, gold, inventory)
    # Show what the Player would have needed
    print("\nTo defeat the 7 Headed Dragon, you would have needed:")
    if gold < 100:
        print(f"-- {100 - gold} more gold coins")
    if health <= 0:
        print(f"-- Health above 0 (You need at least {1 - health} more points)")
    if len(inventory) < 4:
        print(f"-- {4 - len(inventory)} more item(s)")
    if gold >= 100 and health > 0 and len(inventory) >= 4:
        print("-- Actually, you were completely ready! Why didn't You FIGHT!")

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