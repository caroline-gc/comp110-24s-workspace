"""Practice with For Loops and Dictionaries."""

in_stock: dict[str, bool] = {"carrots": True, "beets": False, "apples": True}

for key in in_stock:
    if in_stock[key] is True:   #technically do not need the "is True"
        print(key)