"""Practice with Functions that Mutatate Lists and Dictionaries."""

# removes first element in an input list 
def remove_first(my_list: list[str]) -> None:
    """removes first element in an input list"""
    my_list.pop(0)


# returns forst element of the input list withOUT mutating
def get_first (my_list: list[str]) -> str:
    """Returns first element of the input list withOUT mutating"""
    return my_list[0]

# removes first eement and returns it
def get_and_remove_first(my_list: list[str]) -> str:
    elem: str = my_list[0]
    my_list.pop(0)
    return elem 