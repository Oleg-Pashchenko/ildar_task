import dataclasses
import sys

from models.Vertice import Vertice


class Rect:
    bounds = None

    @dataclasses.dataclass
    class RectBounds:
        left_x: int
        left_y: int
        right_x: int
        right_y: int

    def __init__(self, vertices: list[Vertice]):
        self.__calculate_bounds(vertices)

    def get_bounds(self) -> RectBounds:
        """:return self.bounds"""
        return self.bounds

    def __calculate_bounds(self, vertices: list[Vertice]):
        """Расчет :param self.bounds исходя из vertices"""
        self.bounds = self.RectBounds(
            sys.maxsize, sys.maxsize, -sys.maxsize - 1, -sys.maxsize - 1
        )
        for vertice in vertices:
            if vertice.x < self.bounds.left_x:
                self.bounds.left_x = vertice.x

            if vertice.y < self.bounds.left_y:
                self.bounds.left_y = vertice.y

            if vertice.x > self.bounds.right_x:
                self.bounds.right_x = vertice.x

            if vertice.y > self.bounds.right_y:
                self.bounds.right_y = vertice.y
