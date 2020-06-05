import pygame
import numpy as np
import collections

Point = collections.namedtuple("Point", ["x", "y"])

class FractalTree:
    """Used to draw a binary fractal tree with pygame"""
    def __init__(self, screen, offset_angle: float, min_length: int):
        self.screen = screen
        self.offset_angle = offset_angle
        self.min_length = min_length

    def draw(self, point: Point, angle: float, length: int) -> None:
        """ Draws the fractal tree recursively
        :point: Point, beggining of where line is to be draw
        :angle: float, angle in radians at which the next point will be
        :length: int, how long the next line will be
        """
        x = np.round(np.cos(angle / 180 * np.pi) * length) + point.x
        y = np.round(np.sin(angle / 180 * np.pi) * length) + point.y
        new_point = Point(x, y)
        print(new_point)
        pygame.draw.line(self.screen, (255, 255, 255), point, new_point)

