"""Summing the elements of a list using different loops."""

__author__ = "730394278"

# sums all the elements of the input vals: list[float] and returns the sum.
# For example, w_sum([1.1, 0.9, 1.0]) should compute 1.1 + 0.9 + 1.0 and return the simplified value 3.0

# Version A: Write a function called w_sum that uses a while loop to iterate through vals


def w_sum(vals: list[float]) -> float: 
    """Sums usinga while loop."""
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


# Version B: Write a function called f_sum that uses a for ... in ... loop.


def f_sum(vals: list[float]) -> float:
    """Sums using a for loop."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum 


# Version C: Write a function called f_range_sum that uses a for … in range(0,len(xs)) loop


def f_range_sum(vals: list[float]) -> float:
    """Sums using range."""
    sum: float = 0.0
    for index in range(len(vals)):
        sum += vals[index]
    return sum 


sum_w: float = w_sum([1.1, 0.9, 1.0])
sum_f: float = f_sum([1.1, 0.9, 1.0])
sum_range: float = f_range_sum([1.1, 0.9, 1.0])


print(sum_w)
print(sum_f)
print(sum_range)