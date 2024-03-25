"""EX06: Unit test for dictionary functions."""

__author__ = "730394278"

import pytest

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


# invert: Use Case 1 

def test_invert_use_1() -> None: 
    """Test when empty dict."""
    dict1: dict[str, str] = {}
    assert invert(dict1) == {}


# invert: Use Case 2
    
def test_invert_use_2() -> None: 
    """Test general invert use."""
    dict1: dict[str, str] = {"a": "b", "c": "d"}
    assert invert(dict1) == {"b": "a", "d": "c"}


# invert: Edge Case
    
def test_invert_edge() -> None: 
    """Test when only one item pair in dictionary."""
    dict1: dict[str, str] = {"hello": "world"}
    assert invert(dict1) == {"world": "hello"}


# invert: Key Error Test 
    
def test_invert_key_error() -> None: 
    """Test Key Error."""
    with pytest.raises(KeyError):
        dict1 = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(dict1)
        

# count: Use Case 1
        
def test_count_use_1() -> None: 
    """Test when empty list."""
    list1: list[str] = []
    assert count(list1) == {}


# count: Use Case 2
    
def test_count_use_2() -> None: 
    """Test when there are no duplicates."""
    list1: list[str] = ["yes", "no", "maybe"]
    assert count(list1) == {"yes": 1, "no": 1, "maybe": 1}


# count: Edge Case 1
    
def test_count_edge() -> None: 
    """Test for non str values."""
    list1: list[str] = ["yes", "no", "no", 100]
    assert count(list1) == {"yes": 1, "no": 2, 100: 1}


# favorite_color: Use Case 1
    
def test_favorite_color_use_1() -> None: 
    """Test when empty list."""
    colors: dict[str, str] = {}
    assert favorite_color(colors) == ""


# favorite_color: Use Case 2
    
def test_favorite_color_use_2() -> None: 
    """Test when there is no favorite or most popular color in the list."""
    colors: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "pink"}
    assert favorite_color(colors) == "yellow"


# favorite_color: Edge Case 
    
def test_favorite_color_edge() -> None: 
    """Test when someone does not enter a favorite color in a submission."""
    colors: dict[str, str] = {"Marc": "", "Ezri": "blue", "Kris": "pink", "Caroline": "blue"}
    assert favorite_color(colors) == "blue"


# alphabetizer: Use Case 1
    
def test_alphabetizer_use_1() -> None: 
    """Test when empty list."""
    word_list: list[str] = []
    assert alphabetizer(word_list) == {}


# alphabetizer: Use Case 2
    
def test_alphabetizer_use_2() -> None: 
    """Test for if each words starts with the same letter."""
    word_list: list[str] = ["cat", "car", "cloud"]
    assert alphabetizer(word_list) == {'c': ['cat', 'car', 'cloud']}


# alphabetizer: Edge Case 
    
def test_alphabetizer_edge() -> None: 
    """Test for if an integer is entered as a str."""
    word_list: list[str] = ["cat", "car", "apple", "boy", "100", "123"]
    assert alphabetizer(word_list) == {'c': ['cat', 'car'], 'a': ['apple'], 'b': ['boy'], '1': ["100", "123"]}
   

# update_attendance: Use Case 1
    
def test_update_attendance_use_1() -> None: 
    """Test when starting with an empty dict."""
    attendance_log: dict[str, list[str]] = {}
    update_attendance(attendance_log, "Monday", "Kaleb") 
    assert attendance_log == {"Monday": ["Kaleb"]}


# update_attendance: Use Case 2
    
def test_update_attendance_use_2() -> None: 
    """Test for adding multiple students to the same day at once."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Wednesday", "Vrinda, Kaleb, Alyssa")
    assert attendance_log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Vrinda, Kaleb, Alyssa"]}


# update_attendance: Edge Case 
    
def test_update_attendance_edge() -> None: 
    """Test when adding a new day of the week, but no new names: everone skipped class."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Wednesday", "")
    assert attendance_log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": [""]}


# update_attendance: Edge Case 2
    
def test_update_attendance_edge_2() -> None: 
    """Test when adding a new day of the week, but no new names: everone skipped class."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Alyssa")
    assert attendance_log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    assert attendance_log != {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Alyssa"]}