"""The chanllenge question answer."""
from __future__ import annotations 
__author__ = "730713746"


class Point:
    """Creat the class points."""
    x: float
    y: float
    

    def __init__(self, x_init: float, y_init: float):
        """Construction of the init."""
        self.x = x_init
        self.y = y_init


    def scale_by(self, factor: int):
        """Construction of the scale_by."""
        self.x = self.x * factor
        self.y = self.y * factor

    
    def scale(self, factor: int) -> Point:
        """Construction of the scale."""
        x = self.x * factor 
        y = self.y * factor
        a: Point = Point(x, y)
        return a



