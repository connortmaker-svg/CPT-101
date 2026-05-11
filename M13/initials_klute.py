# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M13 Lab - Working with Strings
# Initial Finder
# ----------------------------------

# Inital User Input
name = input("Enter First and Last Name:  ")

# Strip the name of leading and trailing spacing
c_name = name.strip()
# Seperate the first and last name into a list
name_parts = c_name.split()

# Extract the first character of first and last name from list
first_i = name_parts[0][0].upper()
last_i = name_parts[1][0].upper()

# Put Initials into a string format
initials = f"{first_i}.{last_i}."

print(f"Your Initials are {initials}")