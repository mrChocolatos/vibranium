from abc import ABC, abstractmethod


class Figure(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise AssertionError("Can't add area")
        return self.area + other_figure.area
