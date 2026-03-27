# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M9 Lab - Loop Basics
# Symbol Pattern
# ----------------------------------

# Initial User Input
print("Pattern Table Builder")
symbol = input("What symbol would you like to print to create the table? ")

# Asks for How many Rows
rows = 0
while rows <= 0:
    rows = int(input("How many rows? "))
    if rows <= 0:
        print("Number must be positive.")

# Asks for How Many Columns
cols = 0
while cols <= 0:
    cols = int(input("How many columns? "))
    if cols <= 0:
        print("Number must be positive.")

# Nested loops to print the pattern
for r in range(rows):
    for c in range(cols):
        print(symbol, end="")
    print()