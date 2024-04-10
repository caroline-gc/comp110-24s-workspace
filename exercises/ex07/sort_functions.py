"""Functions that implement sorting algorithms."""

__author__ = "730394278"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm, Insert into an already sorted list."""
    sort_idx = 0
    while sort_idx < len(x) - 1:
        unsort_idx = sort_idx + 1
        while unsort_idx > 0 and x[unsort_idx] < x[unsort_idx - 1]:
            num = x[unsort_idx]
            x[unsort_idx] = x[unsort_idx - 1] 
            x[unsort_idx - 1] = num
            unsort_idx -= 1 
        sort_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm, Repeatedly find the minimum and swap it.""" 
    for idx in range(len(x)):
        min_num = idx
        for elem in range(idx + 1, len(x)):
            if x[elem] < x[min_num]:
                min_num = elem
        if min_num != idx:
            num = x[idx]
            x[idx] = x[min_num]
            x[min_num] = num
    return None