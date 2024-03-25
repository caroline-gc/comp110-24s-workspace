"""EX05 Dictionary Utility Functions."""

___author__ = "730394278"


# invert funtion 

def invert(dict1: dict[str, str]) -> dict[str, str]: 
    """Invert Function."""
    invert_dict: dict[str, str] = {}

    for key in dict1: 
        value = dict1[key]
        if value in invert_dict:
            raise KeyError("error message of your choice here!")
        invert_dict[value] = key
    return invert_dict 


# favortite colors 

def favorite_color(colors: dict[str, str]) -> str:
    """Find most popular color."""
    fav_color: str = ""
    max_count = 0

    for key in colors:
        color = colors[key]
        count = 0

        for elem in colors:
            if colors[elem] == color:
                count += 1

        if count > max_count:
            fav_color = color
            max_count = count
    return fav_color


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


# count function

def count(list1: list[str]) -> dict[str, int]:
    """Count Function."""
    counts: dict[str, int] = {}

    for word in list1:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(count(["yes", "no", "no", "no", "yes"]))


# alpgabetizer

def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Word Alphabetizer Function."""
    alpha_dict: dict[str, list[str]] = {}

    for word in word_list:
        letter1 = word[0].lower()
        if letter1 in alpha_dict:
            alpha_dict[letter1].append(word)
        else: 
            alpha_dict[letter1] = [word]
    return alpha_dict 


print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))
print(alphabetizer(["Python", "sugar", "Turtle", "party", "table"]))

# attendance log 


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance log."""
    if day in attendance_log:
        attendance_log[day].append(student)
    else:
        attendance_log[day] = [student]


attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
update_attendance(attendance_log, "Wednesday", "Kaleb")
print(attendance_log)
