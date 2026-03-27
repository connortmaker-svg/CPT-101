# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M9 Lab - Loop Basics
# Sum of Numbers
# ----------------------------------

print("This program will add all numbers from 1 up through your chosen number.")

# Ensure a positive number
user_num = 0
while user_num <= 0:
    user_num = int(input("What is your number? "))
    if user_num <= 0:
        print("Number cannot be 0 or negative.")

# Calculate the sum
total_sum = 0
for i in range(1, user_num + 1):
    total_sum += i

print(f"The sum of numbers from 1 to {user_num} is {total_sum}.")