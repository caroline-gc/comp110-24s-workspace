"""Game with While Loops."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False 

while correct == False: 
    guess: int = int(input("Guess a Number: "))
    if guess < 1:
        print("too low!")
    if guess > 10:
        print("too high!")
    if guess == SECRET:
        print(f"you got it right! {guess} is the secret number!")
        correct = True
      
    print("Try again!") 