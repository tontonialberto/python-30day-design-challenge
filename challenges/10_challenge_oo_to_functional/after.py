from math import pi
from typing import Callable, List, Literal, Tuple, Union


def rect_area(width: float, height: float) -> float:
    return width * height


def rect_perimeter(width: float, height: float) -> float:
    return 2 * (width + height)


def circle_area(radius: float) -> float:
    return pi * radius**2


def circle_perimeter(radius: float) -> float:
    return 2 * pi * radius


ShapeType = Union[Literal["rect"], Literal["circle"]]


def area_fn(shape: ShapeType) -> Callable[..., float]:
    if shape == "rect":
        return rect_area
    else:
        return circle_area
    

def perimeter_fn(shape: ShapeType) -> Callable[..., float]:
    if shape == "rect":
        return rect_perimeter
    else:
        return circle_perimeter
    

Shape = Tuple[ShapeType, List[float]]


def total_area(shapes: List[Shape]) -> float:
    return sum(area_fn(shape_type)(*shape) for shape_type, shape in shapes)


def total_perimeter(shapes: List[Shape]) -> float:
    return sum(perimeter_fn(shape_type)(*shape) for shape_type, shape in shapes)


def main() -> None:
    shapes: List[Shape] = [
        ("rect", [4, 5]),
        ("rect", [3, 3]),
        ("circle", [2]),
    ]
    print("Total Area:", total_area(shapes))
    print("Total Perimeter:", total_perimeter(shapes))


if __name__ == "__main__":
    main()
