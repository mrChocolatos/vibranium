from src.figure import Figure


class Square(Figure):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Can't create Square")
        super().__init__()
        self.side_a = side
        self.name = f"Square {side}"

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def get_perimeter(self):
        return 4 * self.side_a
