"""Some functions for my garden plan!"""

__author__ = "730394278"

by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
print(by_kind)


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Add a new plant under its kind."""
    if new_plant_kind in by_kind:  # if the kind is already in the dictionary 
        by_kind[new_plant_kind].append(new_plant)
    else:  # if kind is not in the dictionary
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)


by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}


def add_by_date(by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plant under month should be planted."""
    if month in by_date:  # if the kind is already in the dictionary 
        by_date[month].append(plant)
    else:  # if kind is not in the dictionary
        by_date[month] = []
        by_date[month].append(plant)


def lookup_by_kind_and_date(by_kind: dict[str, list[str]], by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return str with list of plants of a specific kind to plant in a specific month."""
    assert kind in by_kind
    assert month in by_date  # or could just use (if kind in plants_by_kind)
    kind_list: list[str] = by_kind[kind]  # list of all my plants of a certain kind input 
    month_list: list[str] = by_date[month]  # list of all plants in a specific month
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:   # nested loop 
            if plant == other_plant:
                combined_list.append(plant)
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:
        return f"No {kind}s to plant in {month}."

