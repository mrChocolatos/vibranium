import math

from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Can't create Circle")
        super().__init__()
        self.radius = radius
        self.name = f"Circle with radius: {radius}"

    @property
    def area(self):
        return int(math.pi * (self.radius ** 2))

    @property
    def get_perimeter(self):
        return int(math.pi * self.radius)
