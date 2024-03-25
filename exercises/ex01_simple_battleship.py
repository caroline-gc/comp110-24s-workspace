"""EX01 - Simple Battleship - A cute step toward Battleship."""
__author__ = "730394278"

# player 1 picks location in range

user_input: str = input("Pick a secret boat location between 1 and 4: ")
user_location: str = str(user_input)

if int(user_input) < 1: 
    print("Error! " + str(user_location) + " too low!") 

if int(user_input) > 4: 
    print("Error! " + str(user_location) + " too high!")

if int(user_input) < 1 or int(user_input) > 4:
    exit()

# player 2 guesses a location in range

user_guess: str = input("Guess a number between 1 and 4: ")
user_number: str = str(user_guess)

if int(user_guess) < 1: 
    print("Error! " + str(user_number) + " too low!")

if int(user_guess) > 4: 
    print("Error! " + str(user_number) + " too high!")

if int(user_guess) < 1 or int(user_guess) > 4:
    exit()

# player 2 guesses location

# create the boxes
   
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

if int(user_input) == int(user_guess) == 1:
    print(RED_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)

if int(user_input) != int(user_guess) == 1:
    print(WHITE_BOX + BLUE_BOX + BLUE_BOX + BLUE_BOX)


if int(user_input) == int(user_guess) == 2:
    print(BLUE_BOX + RED_BOX + BLUE_BOX + BLUE_BOX)

if int(user_input) != int(user_guess) == 2:
    print(BLUE_BOX + WHITE_BOX + BLUE_BOX + BLUE_BOX)


if int(user_input) == int(user_guess) == 3:
    print(BLUE_BOX + BLUE_BOX + RED_BOX + BLUE_BOX)

if int(user_input) != int(user_guess) == 3:
    print(BLUE_BOX + BLUE_BOX + WHITE_BOX + BLUE_BOX)


if int(user_input) == int(user_guess) == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + RED_BOX)

if int(user_input) != int(user_guess) == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + WHITE_BOX)

# player 2 gets feedback

if int(user_guess) == int(user_input):
    print("Correct! You hit the ship.")

if int(user_guess) != int(user_input):
    print("Incorrect! You missed the ship.")