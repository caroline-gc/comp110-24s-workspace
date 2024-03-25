"""Function Practice"""

from random import randint

y: str = print("Hello!")
print(y)

x: int = round(10.25)
print(x)

# definition and syntax

def my_max(number1: int, number2: int) -> int:
    """Returns maximum value out of two numbers"""
    if number1 >= number2:
        return number1
    else: #number1 < number2
        return number2
    

# call the function 
max_number: int = my_max(1,10)
other_max_number: int = my_max(11,3)
print(max_number)