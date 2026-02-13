# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M4 Lab - Python Input/Output
# Cookie Recipe Ingredient Calculator
# ----------------------------------

# Constants for Admin (amount needed to make 10 cookies)
FLOUR = 1 #(cups)
BUTTER = 0.5 #(cups)
SUGAR = 0.75 #(cups)
EGG = 1 #(cups)

# Constants for single (1) cookie, assuming linear recipe
FLOUR_1 = FLOUR / 10
BUTTER_1 = 0.5 / 10
SUGAR_1 = 0.75 / 10
EGG_1 = 1 / 10

#Introduction to Recipe Program
print("\nThis program will help you bake grandma's favorite cookies!\n")

# Needed Variables from user
num_cookies = input("How many Cookies will you need?\nInput the total number you want: ")
cookies_count = int(num_cookies)

# Math needed
total_flour = FLOUR_1 * cookies_count
total_butter = BUTTER_1 * cookies_count
total_sugar = SUGAR_1 * cookies_count
total_eggs = EGG_1 * cookies_count

# Recipe Outputs
print(
    f"\nTo make {cookies_count:.0f} cookies, you will need: \n\n"
    f"{total_flour:.2f} cups(s) of flour\n" 
    f"{total_butter:.2f} cups(s) of butter\n"
    f"{total_sugar:.2f} cups(s) of sugar\n" 
    f"{total_eggs:.0f} egg(s) [Utilize only {total_eggs:.2f} of the egg(s)]\n"  
)