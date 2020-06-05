import pygame
import numpy as np
import collections

Point = collections.namedtuple("Point", ["x", "y"])

class FractalTree:
    """Used to draw a binary fractal tree with pygame"""
    def __init__(self, offset_angle: float, min_length: int):
        self.offset_angle = offset_angle
        self.min_length = min_length

