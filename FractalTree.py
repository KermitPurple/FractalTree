import pygame
import numpy as np
import collections

Point = collections.namedtuple("Point", ["x", "y"])

class FractalTree:
    """Used to draw a binary fractal tree with pygame"""
    def __init__(self, screen, offset_angle: float, min_length: int, length_divisor: float):
        self.screen = screen
        self.offset_angle = offset_angle
        self.min_length = min_length
        self.length_divisor = length_divisor

    def draw(self, point: Point, angle: float, length: int) -> None:
        """ Draws the fractal tree recursively
        :point: Point, beggining of where line is to be draw
        :angle: float, angle in radians at which the next point will be
        :length: int, how long the next line will be
        :returns: None
        """
        x = np.round(np.cos(angle / 180 * np.pi) * length) + point.x
        y = np.round(np.sin(angle / 180 * np.pi) * length) + point.y
        new_point = Point(x, y)
        if FractalTree.distance(point, new_point) > self.min_length:
            pygame.draw.line(self.screen, (255, 255, 255), point, new_point)
            self.draw(new_point, angle + self.offset_angle, length // self.length_divisor)
            self.draw(new_point, angle - self.offset_angle, length // self.length_divisor)

    @staticmethod
    def distance(p1: Point, p2: Point) -> int:
        """ Return distance between two points using distance formula
        :p1: Point, first point to be compared
        :p2: Point, second point to be compared
        :returns: int, rounded distance between p1 and p2
        """
        return np.round(np.sqrt(((p2.x - p1.x) ** 2) + ((p2.y - p1.y) ** 2)))
