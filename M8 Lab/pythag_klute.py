# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M8 Lab - Loop Basics
# Pythagoream Therom Calculator
# ----------------------------------

import math # Importing math functionality

print('Pythagorean Theorem Solver\n')

# Side A user input
a = 0
while a <=0:
    a = float(input("Enter the lenght of side A:  "))
    if a <= 0:
        print("Side A must be positive")

# Empty print for cleaniness
print()

# Side B user input
b = 0
while b <=0:
    b = float(input("Enter the lenght of side B:  "))
    if b <= 0:
        print("Side B must be positive")

# Pythagoream Calcualtion of side C
c = math.sqrt((a ** 2) + (b ** 2))

# User Outputs
print(f"Side A: {a:.2f}")
print(f"Side B: {b:.2f}")
print(f"Side C: {c:.2f}")
    