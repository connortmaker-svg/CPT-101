# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 2
# Generating Shapes with Turtle
# ----------------------------------

import turtle # For the main thing of the program

def get_menu_input(is_new_run):
    # Create a Menu for the USER to interact with
    if is_new_run:
        print("\nShape Drawing Program")

    # inital variable to check against
    choice = 0
    
    while choice != 1 or choice != 2 or choice != 3 or choice !=4:
        print("\n This program can draw three different shapes\n")
        print("1. Draw Circle")
        print("2. Draw Square")
        print("3. Draw Equilateral Triangle")
        print("4. Exit Program")

        try: 
            choice = int(input("Which taks would you like to perform?  "))
            if choice >= 1 and choice <= 4:
                return choice
            else:
                print("\nNot Valid Menu Option")
        except ValueError:
            print("\nNot a Valid Menu Option")
            choice = 0 # Resets the choice is an invalid number


def get_color():
    # Prompts the User for what Color to input
    print()
    color = input("What Color would you like the shape to be? (red, orange, purple)").lower().strip()
    while color != "red" and color != "orange" and color != "purple":
        print("Not a Valid Option")
        color = input("What Color would you like the shape to be? (red, orange, purple)").lower().strip() 
    return color

def get_coords(axis_name, min_val, max_val):
    # Prompts User for the x and y coordinates of the start point and ensures it fits in the given window
    
    # Initial Values to Check Against
    
    valid_input = False
    val = 0

    while not valid_input:
        try:
            val = int(input(f"What is the {axis_name} value for your desired start location? ({min_val} to {max_val}) "))
            if min_val <= val <= max_val:
                valid_input = True # True if the Coordinates are within Bounds
            else:
                print("Not Valid Input \n")
        except ValueError:
            print("Not Valid Input")
    return val

def get_size(choice, min_val, max_val):
    # Prompts the User for the Radius or Side Length Based on the Shape input
    if choice == 1:
        print("Input a Radius to draw the Circle\n")
        prompt = f"What is the radius? ({min_val} to {max_val}) "
        reprompt = f"What is the radius? ({min_val} to {max_val})"
        error_msg = f"Please select a value between {min_val} and {max_val}.\n"
    elif choice == 2:
        print("Input a Length of the Side to draw the Square\n")
        prompt = f"What is the length of the side? ({min_val} to {max_val}) "
        reprompt = f"What is the length of the side? ({min_val} to {max_val}) "
        error_msg = f"Please select a value between {min_val} and {max_val}.\n"
    elif choice == 3:
        print("Input a Length of the Side to draw the Triangle\n")
        prompt = f"What is the length of the side? ({min_val} to {max_val}) "
        reprompt = f"What is the length of the side? ({min_val} to {max_val})"
        error_msg = f"Please select a value between 0 and {max_val}.\n"

    # Initial variables to check against (Notice these are aligned to the left!)
    valid_input = False
    size = 0
    first_prompt = True

    # Loop To Check if the inputs are valid
    while not valid_input:
        try:
            if first_prompt:
                size = int(input(prompt))
                first_prompt = False
            else: 
                size = int(input(reprompt))
            
            if min_val <= size <= max_val:
                valid_input = True
            else:
                print(error_msg)
                first_prompt = False
        except ValueError:
            print(error_msg)
            first_prompt = False
            
    return size

def draw_circle(x, y, radius, color):
    # Setup the Pen
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)

    # Draw the Circle
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_square(x, y, side, color):
    # Setup the Pen
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)

    #Draw the Square
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()

def draw_triangle(x, y, side, color):
    # Setup the Pen
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)

    # Begin Drawing the Triangle
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

def main():
    # Setup the Main Turtle Windows
    turtle.setup(600,600)

    # Constants to Check Against
    MIN_COORD = -300
    MAX_COORD = 300
    MIN_SIZE = 1
    MAX_SIZE = 300

    is_first_run = True
    choice = 0 

    # Main Loop to Start Program
    while choice != 4:
        # Starts the Menu
        choice = get_menu_input(is_first_run)
        is_first_run =  False

        if choice == 4:
            print("\nGoodBye")
            turtle.bye()
        else:
            # The Condition if the User didn't Exit the Program

            # Get user Input with Color
            color = get_color()

            # Get User Input with Coordinates
            print("\nThe Starting Position is in the Center of the Window (0,0)")
            x = get_coords('x', MIN_COORD, MAX_COORD)
            print()
            y = get_coords('y', MIN_COORD, MAX_COORD)
            print()

            # Get User Input of Size
            size = get_size(choice, MIN_SIZE, MAX_SIZE)

            # Extra Line to Say it's Doing Something
            print("\nDrawing Shape in the Turtle Window.....")

            # Choose Which Shape to Draw Based on User Input
            if choice == 1:
                draw_circle(x, y, size, color)
            elif choice == 2:
                draw_square(x, y, size, color)
            elif choice == 3:
                draw_triangle(x, y, size, color)
             
main()