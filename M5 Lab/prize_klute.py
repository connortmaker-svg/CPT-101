# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M5 Lab - Python Input/Output
# Prizes
# ----------------------------------

# Initial Inquiry
print("Prize Inquiry\n")
user_score = int(input("Input your Score:"))

# Logic
if user_score > 50:
    print("WOW you broke the score charts.....\n Not a valid score")

elif 41 <= user_score <= 50:
    print("You get a Gold Medal!")

elif 31 <= user_score <= 40:
    print("You get a Silver Medal!")
    gold = 41 - user_score
    print(f"You only need {gold} points to get to Gold!")

elif 21 <= user_score <= 30:
    print("You get a Bronze Medal!")
    silver = 31 - user_score
    print(f"You only need {silver} points to get to Silver!")

elif 11 <= user_score <= 20:
    print("You get an Honorable Mention!")
    bronze = 21 - user_score
    print(f"You only need {bronze} points to get to Bronze!")

elif 0 <= user_score <= 10:
    print("Unfortunatly no prize...")
    honor = 11 - user_score
    print(f"You only need {honor} points to get to an Honorable Mention")

elif user_score < 0:
    print("Do you know negatives aren't valid???")