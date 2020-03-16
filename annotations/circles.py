import math
from typing import List, Union, Tuple, Dict

Rational = Union[int, float]
Id = Union[int, str]


def safe_radius_of(number: Rational) -> Rational:
    if not (
            isinstance(number, int) or
            isinstance(number, float)
    ):
        raise TypeError('Radius should be either "int" or "float" data type!')
    if number < 0:
        raise ValueError('Radius value should be more that "0"!')
    return number


def calculate_square_of(number):
    return number ** 2


def multiply_by_pi(number: Rational):
    return math.pi * number


def double_of(number):
    return number * 2


class Circle:
    def __init__(self, identifier: Id, radius: Rational, color: str):
        self.identifier = identifier
        self._radius = lambda: safe_radius_of(radius)
        self._color = color

    def change_color(self, color: str):
        if not isinstance(color, str):
            raise TypeError('Color should be "str" data type!')
        self._color = color

    def diameter(self):
        return double_of(self._radius())

    def area(self):
        return multiply_by_pi(calculate_square_of(self._radius()))

    def perimeter(self):
        return double_of(multiply_by_pi(self._radius()))

    def __str__(self):
        return f'Circle(radius={self._radius()}, color="{self._color}")'


class Circles:
    def __init__(self, circles: Tuple[Circle]):
        self._circles = circles

    def update_colors(self, new_colors: Dict[str, str]) -> None:
        for identifier, color in new_colors.items():
            this = self.find(identifier)
            this.change_color(color)
            print(this)

    def find(self, identifier: str) -> Circle:
        for this in self._circles:
            if this.identifier == identifier:
                return this

        raise ValueError(f"There is no circle with this identifier: {identifier}")

    def show_diameters(self) -> None:
        for circle in self._circles:
            print(f"A diameter of {circle} is {circle.diameter()}")

    def show_areas(self) -> None:
        for circle in self._circles:
            print(f"An area of {circle} is {circle.area()}")

    def show_perimeters(self) -> None:
        for circle in self._circles:
            print(f"A perimeter of {circle} is {circle.perimeter()}")


if __name__ == "__main__":
    circles = Circles(
        Circle(1, 1, 'red'),
        Circle("2", 0.2, 'super-red'),
        Circle(3, 3, 'green'),
        Circle(4, 5, 'super-green'),
    )
    circles.show_diameters()
    circles.show_areas()
    circles.show_perimeters()
    circles.update_colors([
        'blue',
        'red',
        'black',
        'purple'
    ])