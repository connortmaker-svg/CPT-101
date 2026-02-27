# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M5 Lab - Python Input/Output
# Clothing Selector
# ----------------------------------

# Constants
HIGH_TEMP = 70
LOW_TEMP = 40

# User Inputs
print("I am you personal assistant. Time to dress\n\n")
input = int(input("Please input the current project high temperature for today:  "))

# Logic
# Checks for Temps above 70, inbetween 40 and 70, and below 40
if input >= HIGH_TEMP:
    print("Pants are Bad")
elif LOW_TEMP < input < HIGH_TEMP:
    print("Pants are Recommended")
elif input <= LOW_TEMP:
    print("Pants are essential")
else:
    print("might be broken")