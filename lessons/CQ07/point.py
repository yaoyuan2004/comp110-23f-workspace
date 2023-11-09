"""The chanllenge question answer."""
from __future__ import annotations 
__author__ = "730713746"


class Point:
    """Creat the class points."""
    x: float
    y: float

    def __init__(self, x_init: float = 0, y_init: float = 0):
        """Construction of the init."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> Point:
        """Construction of the scale_by."""
        self.x = self.x * factor
        self.y = self.y * factor
        return self

    def scale(self, factor: int) -> Point:
        """Construction of the scale."""
        x = self.x * factor 
        y = self.y * factor
        a: Point = Point(x, y)
        return a
    
    def __str__(self) -> str:
        """Defind the new str methods."""
        my_str = f"x: {self.x}; y: {self.y}"
        return my_str
    
    def __mul__(self, factor: int | float) -> Point:
        """Defind the new mul methods."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __add__(self, factor: int | float) -> Point:
        """Defind the new add methods."""
        new_point: Point = Point(self.x + factor, self.y + factor)
        return new_point