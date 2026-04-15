# ----------------------------------
# Connor Klute
# CPT 101 - Shaffer
# Project 2
# Rock Paper Scissors
# ----------------------------------

import random # For randomness

def get_user_input():
    # Set Values to Check against User Input
    valid_in = False
    choice = -1
    
    # Loop to Check User Input
    while not valid_in:
        try:
            print("\nEnter 1 for Rock, 2 for Paper, 3 for Scissor, or 0 to EXIT")
            choice = int(input())

            if choice >= 0 and choice <= 3:
                valid_in = True
            else:
                print("Invalid Input. Try Again")
        except ValueError:
            print("Invalid Input. Try Again")
    return choice


def get_com_choice():
    return random.randint(1,3)

def choose_winner(user_choice, com_choice):
    # Constants for each choice of rock,paper,scissors
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    # Converting User Number to a string
    if user_choice == ROCK:
        user_str = "Rock"
    elif user_choice == PAPER:
        user_str = "Paper"
    else:
        user_str = "Scissors"
    
    # Converting Computers Number to a string
    if com_choice == ROCK:
        com_str = "Rock"
    elif user_choice == PAPER:
        com_str = "Paper"
    else:
        com_str = "Scissors"

    # Tie Choice
    if user_choice == com_choice:
        print(f"You both chose {user_str}. It's a tie!")
        return False
    
    # Main Win Logic Block for Rock, Paper, Scissors
    elif (user_choice == ROCK and com_choice == SCISSORS) or \
         (user_choice == PAPER and com_choice == ROCK) or \
         (user_choice == SCISSORS and com_choice == PAPER):
        print(f"You chose {user_str}. Computer chose {com_str}. You win!")
        return True
    
    # Lose Block Logic
    else:
        print(f"You chose {user_str}. Computer chose {com_str}. You lose!")
        return False

# Main Game Loop
def main():
    # Constants with temp value
    user_win = 0
    keep_playing = True

    print("PLAY ROCK, PAPER, SCISSORS!")

    # Main Loop
    while keep_playing:
        user_choice = get_user_input()
        if user_choice == 0:
            # Ends the Loop 
            keep_playing = False
        else:
            com_choice = get_com_choice()
            win = choose_winner(user_choice, com_choice)

            if win:
                user_win += 1
    
    # End of Loop
    print(f"\nYou won {user_win} matches. Goodbye.")

main()