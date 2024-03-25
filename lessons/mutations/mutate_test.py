"""Test my mutating Functions."""

from lessons.mutations.mutating_functions import get_first, remove_first, get_and_remove_first

#Use Case for remove_first

def test_remove_first_use_case() -> None: 
    """test basic use case for remove_first function."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    remove_first(t) 
    t == ["rainy", "sunny"]


def test_get_first_use_case() -> None:
    """Test for get first."""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    ret_value: str = get_first(t)
    assert t == ["cloudy", "rainy", "sunny"]
    assert ret_value == "cloudy"

def test_get_and_remove_first_use_case() -> None:
    """tests function"""
    t: list[str] = ["cloudy", "rainy", "sunny"]
    ret_value: str = get_and_remove_first(t)
    assert t == ["rainy", "sunny"]
    assert ret_value == "cloudy"