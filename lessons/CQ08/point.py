"""CQ08: Object Oriented Programming."""

from __future__ import annotations

__author__ = "730394278"


class Point:
    """making a Point class."""

    x: float
    y: float 

    def __init__(self, x_init: float, y_init: float):
        """Create a New Point Object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that mutates a Point."""
        self.x *= factor
        self.y *= factor 

    def scale(self, factor: int) -> Point:
        """Method that belongs to the Point class."""
        coordinate: Point = Point(self.x, self.y)
        coordinate.x = self.x * factor
        coordinate.y = self.y * factor
        return coordinate
    