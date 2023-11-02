"""The chanllenge question answer."""
from __future__ import annotations 
__author__ = "730713746"


class Point:
    """Creat the class points."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init


    def scale_by(self, factor: int):
        x = x * factor
        y = y * factor

    
    def scale(self, factor: int) -> Point:
        x = self.x * factor 
        y = self.y * factor
