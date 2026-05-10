# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# M12 Lab - Lists
# Square and Cubes
# ----------------------------------

# Getting the Scores from the user
def get_num():
    # ask the user for the number of scores, then collects each one
    num_count = int(input("How many scores do you have?  "))
    # Empty List
    og_list = []
    # Main Loop
    for i in range(num_count):
        num = float(input(f"Input Score {i+1}:   "))
        og_list.append(num)
    return og_list

# Takes a list of numbers and returns new list with values squared
def calc_square(numbers):
    sq_list = []
    for number in numbers:
        sq_list.append(number ** 2)
    return sq_list

# Takes a list of numbers and returns new list with values cubed
def calc_cube(numbers):
    cu_list = []
    for number in numbers:
        cu_list.append(number ** 3)
    return cu_list

def main():
    # Get User list
    og_list = get_num()

    # Calc New Lists
    sq_list = calc_square(og_list)
    cu_list = calc_cube(og_list)

    # Display Results
    print(f"Original List: {og_list}")
    print(f"Squared List: {sq_list}")
    print(f"Cubed List: {cu_list}")

main()