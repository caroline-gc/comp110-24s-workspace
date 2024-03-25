"""Practice with Dictionaries."""

# empty dictionary
ice_cream: dict[str, int] = dict()


ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
#can also use single quotes if you want

#add items to dict
ice_cream["mint"] = 3

#remove element 
ice_cream.pop("mint")

print(ice_cream)


#Accessing
print(ice_cream["vanilla"])
print(f"Number of vanilla: {ice_cream['vanilla']}")  #syntax for using f string 

#Updating/Modifying Values
ice_cream["vanilla"] += 1
print (ice_cream)
print(f"Number of vanilla: {ice_cream['vanilla']}")  #syntax for using f string 

#how to check if there is a specific key in tthe dictionary
print("mint" in ice_cream)

ice_cream["pecan"]

