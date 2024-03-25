"""List Syntax Practice"""

#initialize an empty list 

grocery_list: list[str] = list() # <- list constructor
grocery_list: list[str] = [] # <- literal

print(grocery_list)

# add item to list

grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print("after appending: ")
print(grocery_list)

# OR USE THIS METHOD VVV

#initializing an already populated list

grocery_list2: list[str] = ["bananas", "milk", "bread"]

print("populated list: ")
print(grocery_list2)

grocery_list2.append("eggs")
print(grocery_list2)

# Indexing

print("print frst element of string: ")
print(grocery_list2[0])

# Modifying by index

print("Before change: ")
print(grocery_list2)
grocery_list2[1] = "almond milk"
print("After change: ")
print(grocery_list2)

# Length of a list

print(len(grocery_list2))

# Remove Iten from a list
grocery_list2.pop(1)
print("After removing almond milk")
print(grocery_list2)

# Function using lists
# Function name: display
# Parameter: list[str]
# Return nothing 
# Print the list

def display(word:list[str]) -> None:
    print(display)

display(grocery_list2)

x = display(["Alyssa", "Erin", "AK"])
print(x) # this would return none because we did not specifiy a return


# Function that creates a list
# Name: create
# parameters: str and str
# return: list of strings
# put both parameters into a list


def create(item1: str, item2: str) -> list[str]: 
    my_list: list[str] = [item1, item2]
    return my_list

print(create("Hello", "World"))

print(grocery_list2[10])


