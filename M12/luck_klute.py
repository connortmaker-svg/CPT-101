# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M12 Lab - Lists
# Lucky Word
# ----------------------------------

import random # For using Randomness within the program

def main():
    # The List that will be manipulated
    tools = [
        "calipers", 
        "soldering iron", 
        "3D printer", 
        "laser engraver", 
        "multimeter", 
        "Raspberry Pi", 
        "microcontroller", 
        "wire stripper", 
        "oscilloscope", 
        "hot glue gun"      
    ]

    # User Prompt and Input
    print("Enter a number to get your lucky tool")
    user_input = int(input("or enter 0 to have one ranomly chosen:  "))

    # Main loop that handles the 0 condition
    if user_input == 0:
        luck = random.choice(tools)
    else:
        luck = tools[input - 1]
    # Outcome
    print(f"You Lucky tool is a {luck}.")

main()