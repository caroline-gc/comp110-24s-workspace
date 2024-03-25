"""EX02 - One-shot Battleship!"""

__author__ = "730394278"

# Emojis 

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# grid parameters and ship location 

grid_size = 4
secret_row = 3
secret_column = 2

# have user guess row

guess_row = int(input("Guess a row: "))

while guess_row < 1 or guess_row > grid_size:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# have user guess column

guess_column = int(input("Guess a column: "))

while guess_column < 1 or guess_column > grid_size:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

# box color

if guess_row == secret_row and guess_column == secret_column:
    box = RED_BOX
else:
    box = WHITE_BOX

# create a counter system for grid
    
row_counter = 1

while row_counter <= grid_size:
    row_str = str("")
    col_counter = 1

    # evaluate row and column guess

    if row_counter == guess_row:
        while col_counter <= grid_size:
            if col_counter == guess_column:
                row_str += box  
            else:
                row_str += BLUE_BOX  
            col_counter += 1
    else:
        while col_counter <= grid_size:
            row_str += BLUE_BOX 
            col_counter += 1

    print(row_str)
    row_counter += 1

# user guess outcome
    
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")