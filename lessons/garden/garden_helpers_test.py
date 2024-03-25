"""Test my garden functions."""

__author__ = "730394278"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date

# Unit Tests for add-by_kind


def test_add_by_kind_edge() -> None: 
    """Add a new kind and new plant."""
    by_kind = {"flower": ["marigold"]}
    add_by_kind(by_kind, "fruit", "apple")
    assert by_kind == {"flower": ["marigold"], "fruit": ["apple"]}


def test_add_by_kind_use() -> None: 
    """Add plant to existing kind."""
    by_kind = {"flower": ["marigold"]}
    add_by_kind(by_kind, "flower", "rose")
    assert by_kind == {"flower": ["marigold", "rose"]}


# Unit Tests for add_by_date


def test_add_by_date_edge() -> None: 
    """Add plant to month with no plants."""
    by_date = {"April": ["marigold"]}
    add_by_date(by_date, "May", "daisy")
    assert by_date == {"April": ["marigold"], "May": ["daisy"]}
    

def test_add_by_date_use() -> None: 
    """Add plant to moth with plants already."""
    by_date = {"April": ["marigold"]}
    add_by_date(by_date, "April", "rose")
    assert by_date == {"April": ["marigold", "rose"]}


# Unit Tests for lookup_by_kind_and_date


def test_lookup_by_kind_and_date_empty() -> None: 
    """No plants with kind and month."""
    by_kind = {"flower": ["marigold", "rose"]}
    by_date = {"April": ["marigold"], "June": []}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "June") == "No flowers to plant in June."
    

def test_lookup_by_kind_and_date_use() -> None: 
    """Plant of kind in month."""
    by_kind = {"flower": ["marigold", "rose"]}
    by_date = {"April": ["marigold", "rose"]}
    assert lookup_by_kind_and_date(by_kind, by_date, "flower", "April") == "flowers to plant in April: ['marigold', 'rose']"
