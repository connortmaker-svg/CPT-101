# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M13 Lab - Working with Strings
# Character Counter
# ----------------------------------

# Prompt the User to input a Sentance and Character to Find
sent = input("Enter a sentence:  ")
char = input("Enter a Character to find:  ")

# Count how many times the user character exsist
time_exsist = sent.count(char)

# Find the 'index' of the first appearance of the character
index = sent.find(char)

# Main question
if time_exsist <= 0:
    print(f"No {char} character(s) were found")
else:
    print(f"Your Character appears {time_exsist} times in your sentance")
    print(f"Your charcter first appears at index {index}")