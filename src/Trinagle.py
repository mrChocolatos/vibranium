from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        if side_a >= (side_b + side_c) or side_b >= (side_a + side_c) or side_c >= (side_b + side_a):
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle a = {side_a}, b = {side_b}, c = {side_c}"
        self.p = (1/2)*(self.side_a + self.side_b + self.side_c)
        super().__init__()

    @property
    def get_area(self):
        return (self.p * (self.p - self.side_a) * (self.p - self.side_b) * (self.p - self.side_c))**0.5

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
