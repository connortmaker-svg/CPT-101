# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M9 Lab - Loop Basics
# Math Menu
# ----------------------------------

import math #To do Math Stuff

choice = 0

while choice != 3:
    print("\nMath Menu")
    print("Choose an option from the menu below:")
    print("1. Square Root Calculator")
    print("2. Power of 2 Caculator")
    print("3. Exit Program")

    choice = int(input("Enter a menu option between 1 and 3:  "))

    if choice == 1:
        num = float(input("Enter a number to find the square root: "))
        result = math.sqrt(num)
        print(f"The square root of {num} is {result:.2f}")
    elif choice == 2:
        num = float(input("Enter a number to find its square: "))
        result = num ** 2
        print(f"{num} squared is equal to {result}.")
    elif choice == 3:
        print("Goodbye.")
    else:
        # Reject values that are not part of the menu
        print("This is not a valid menu option. Try again.")