# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 2
# Generating Shapes with Turtle
# ----------------------------------

import turtle # For the 

def get_menu_input(is_new_run):
    # Create a Menu for the USER to interact with
    if is_new_run:
        print("\nShape Drawing Program")
    
    while True:
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


def get_color():
    # Prompts the User for what Color to input
    print()
    color = input("What Color would you like the shape to be? (red, orange, purple)").lower().strip()
    while color != "red" or color != "orange" or color != "purple":
        print("Not a Valid Option")
        color = input("What Color would you like the shape to be? (red, orange, purple)").lower().strip()
    return color

def get_coords(axis_name, min_val, max_val):

def get_size(choice, min_val, max_val):

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


main()