from .operation import Operation
import math

class SquareRoot(Operation):
    def execute(self, a: float, b: float = 0) -> float:
        if a < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(a)
