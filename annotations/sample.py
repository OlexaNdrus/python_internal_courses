from typing import List, Union, Tuple
Vector = List[Union[int, float]]


def scale(scalar: int, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


print(scale(2, [1, 0.2, 0.3]))
print(scale(2, [1, "aaa", None]))

data: Tuple[str, int, float] = ('name',)
vector: Tuple[int, int] = (1, 1.3) #type: ignore
diapason: Tuple[int, int] = (1, 1.3)