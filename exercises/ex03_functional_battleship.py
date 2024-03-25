"""EX03 - Functional Battleship!"""

__author__ = "730394278"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Create function for evaluating player's guess


def input_guess(grid_size: int, guess_type: str) -> int:
    """Evaluate User Input."""
    assert guess_type == "row" or guess_type == "column"
    guess = int(input(f"Guess a {guess_type}: "))
    while True:   
        if 1 <= guess <= grid_size:
            return guess
        else: 
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try Again: "))
        
# Create function for the emoji grid set up 


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None: 
    """Print out Battleship Board."""
    row = 1

    while row <= grid_size:
        row_output = ""
        column = 1
        while column <= grid_size:
            if row == row_guess and column == column_guess:
                if correct:
                    row_output += RED_BOX
                else:
                    row_output += WHITE_BOX
            else:
                row_output += BLUE_BOX
            column += 1
        print(row_output)
        row += 1

# Create function for evaluation of a correct guess


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Check if correct guess."""
    return row_guess == secret_row and column_guess == secret_column

# Create a main function that combines input_guess, print_grid, and correct_guess into a main game function


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Game Loop."""
    turns = 0

    while turns < 5:
        turns += 1
        print(f"=== Turn {turns}/5 ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correct)
        if correct:
            print(f"Hit! You won in {turns}/5 turns!")
            return
        else:
            print("Miss!")
    print("X/5 - Better luck next time!")

# make it so the grid size and location is different each time 


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
