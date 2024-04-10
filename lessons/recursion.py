"""CQ07 Recursion."""

__author___ = "730394278"


def f(n:int, k:int) -> int: 
    """Recursive."""
    if n == 0 or k == 0: 
        return 0
    else: 
        return f(n - 1, k) + k
