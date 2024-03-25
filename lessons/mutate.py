"""Mutating functions."""
__author__ = "730394278"

# Part 1 manual_append()


def manual_append(birth_month: list[int], day: int) -> None:
    """Add a new integer to an existing list of integers."""
    birth_month.append(day)


birth_date: list[int] = [0, 0, 7]

manual_append(birth_date, 22)
print(birth_date)

# Part 2.double()


def double(list1: list[int]) -> None:
    """Double the integers in a list."""
    orig_index: int = 0

    while orig_index < len(list1):
        list1[orig_index] = list1[orig_index] * 2
        orig_index += 1 
    
    
original: list[int] = [1, 2, 3]

double(original)
print(original)
