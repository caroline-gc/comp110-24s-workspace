"""Splitting a dictionary into two lists."""

__author__ = "730394278"

# get_keys makes a list of all of the keys in a dictionary 


def get_keys(param: dict[str, int]) -> list[str]:
    """Make a list of Keys."""
    keys = list()
    for key in param:
        keys.append(key)
    return keys


# get_values makes a list of all oof the values in a dict


def get_values(param: dict[str, int]) -> list[int]:
    """Make a list of Values."""
    values = list()
    for key in param:
        values.append(param[key])
    return values 


test: dict[str, int] = {"Hello": 1, "World": 2}


print(get_keys(test))
print(get_values(test))