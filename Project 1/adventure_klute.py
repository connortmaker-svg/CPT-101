# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 1 - M1 - M6
# Choose your Own Adventure
# ----------------------------------

print("INTRO THINGIES")
print("descriptions")
print("Branch 1 start")
print("branch 2 start")
print("branch 3 start")

# User input for initial choice
int_choice = input("\nChoice 1, 2, or 3")

# Branch 1 Start
if int_choice == "1":
    print("description")
    print("Branch 1.1 start")
    print("branch 1.2 Start")
    print("branch 1.3 start")

    choice_21 = input("\n Where to go next")
    if choice_21 == "1":
        print("Outcome 1.1")
    elif choice_21 == "2":
        print("outcome 1.2")
    elif choice_21 == "3":
        print("outcome 1.3")
    else:
        print("WRONG")

# Branch 2 Start
elif int_choice == "2":
    print("description")
    print("Branch 2.1 start")
    print("branch 2.2 Start")
    print("branch 2.3 start")

    choice_22 = input("\n Where to go next")
    if choice_22 == "1":
        print("Outcome 2.1")
    elif choice_22 == "2":
        print("outcome 2.2")
    elif choice_22 == "3":
        print("outcome 2.3")
    else:
        print("WRONG")

# Branch 3 Start
elif int_choice == "3":
    print("description")
    print("Branch 3.1 start")
    print("branch 3.2 Start")
    print("branch 3.3 start")
    
    choice_23 = input("\n Where to go next")
    if choice_23 == "1":
        print("Outcome 3.1")
    elif choice_23 == "2":
        print("outcome 3.2")
    elif choice_23 == "3":
        print("outcome 3.3")
    else:
        print("WRONG")

else:
    print("You died")