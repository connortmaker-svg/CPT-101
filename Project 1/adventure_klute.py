# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 1 - M1 - M6
# Choose your Own Adventure - Mishaps of a Knight
# ----------------------------------

print("The Mishaps of a 'Knight'")
print("A massive blue dragon is terrorizing the local town, and you have been chosen as the knight to take it down.\n")
print("You stand at the entrance of the dark, smoky cave.\n")
print("What do you do?\n")
print("1. Enter the Cave with a sword.")
print("2. Enter the Cave with a custom built gadget")
print("3. Turn back and go the tavern for a drink")

# User input for initial choice
int_choice = input("\nWhat is your choice? Enter 1, 2, or 3 to continue: ")

# Branch 1 Start
if int_choice == "1":
    print("\nYou enter with the sword, but it is extremely dark in the cave!/\n")
    print("1. Swing blindly into the shadows.")
    print("2. Shout a challenge to the dragon.")
    print("3. Sneak behind a stalagmite.")
    choice_21 = input("\nHow do you proceed?  ")

    # Secondary choices of Branch 1 starting
    if choice_21 == "1":
        print("\nYou hit a rock. The vibration breaks your leg, immobilizing you. The dragon eats you.")
    elif choice_21 == "2":
        print("\nThe dragon finds your challenge hilarious. Then it eats you.")
    elif choice_21 == "3":
        print("\nYou trip over your own scabbard, waking the dragon. The dragon eats you")
    else:
        print("\nInvalid Input: You have frozen in fear and have become a statue to stand on for eons")

# Branch 2 Start
elif int_choice == "2":
    print("\n You enter with your gadget in hand, however the battery starts smoking!\n")
    print("1. Try to recalibrate the gadget.")
    print("2. Throw the gadget at the dragons' snout")
    print("3. Use the gadget as a flashlight")
    choice_22 = input("\n What do you do?!  ")

    # Secondary choices of Branch 2 starting
    if choice_22 == "1":
        print("\nYou get a Blue Screen of Death. While distracted the dragon eats you")
    elif choice_22 == "2":
        print("\nThe gadget bounces off the dragon, not inflicting any harm whatsoever. The dragon isn't amused, and proceeds to eat you.")
    elif choice_22 == "3":
        print("\nYou had it pointing the wrong way!! You are now blinded, and the dragon then eats you.")
    else:
        print("\nInvalid Input: Your gadget short circuits and electrocutes you where you stand.")

# Branch 3 Start
elif int_choice == "3":
    print("\nYou have decided that the dragon is not worth it. You head down to the 'Salty Spitoon'for a drink\n")
    print("1. Order a glass of a suspicious liquid.")
    print("2. Challenge the local blacksmith to a duel.")
    print("3. Sit by the fireplace to warm up.")
    choice_23 = input("\n What do you want to do?")
    # Secondary choices of Branch 3 starting
    if choice_23 == "1":
        print("\nThe drink was actually a poison that an evil witch had left behind. You have died from poisoning")
    elif choice_23 == "2":
        print("\nThe blacksmith is a Tibetan Monk. He ends your journey with a single punch.")
    elif choice_23 == "3":
        print("\nA spark jumps from the fire and ignites your cloak and you. You have been toasted")
    else:
        print("\nInvalid Input: You stood in the doorway too long and got trampled by a horse")

else:
    print("Invalid Input: You have won the game!")