"""EX04 Utils."""

__author__ = "730394278"

# all


def all(list0: list[int], num: int) -> bool:
    """All Function."""
    if len(list0) == 0: 
        return False
    idx = 0
    while idx < len(list0):
        if list0[idx] != num:
            return False
        idx += 1
    return True 


print(all([1, 1, 1], 1))


# max


def max(param: list[int]) -> int:
    """Max Function."""
    if len(param) == 0:
        raise ValueError("max() arg is an empty List")
    highest_num: int = param[0]
    idx: int = 1 
    while idx < len(param):
        if param[idx] > highest_num:
            highest_num = param[idx]
        idx += 1
    return highest_num


print(max([2, 9, 1]))


# is_equal


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Is_Equal Function."""
    if len(list1) != len(list2):
        return False
    idx = 0 
    while idx < len(list1):
        if list1[idx] != list2[idx]:
            return False 
        idx += 1
    return True


print(is_equal([1, 0, 1], [1, 0, 1]))


# extend


def extend(list3: list[int], list4: list[int]) -> None:
    """Extend Function."""
    idx = 0
    while idx < len(list4):
        list3.append(list4[idx])
        idx += 1
    return None


extend([1, 2, 3], [4, 5, 6])
