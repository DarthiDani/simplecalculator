import math

class Logarithm:
    def execute(self, a: float, b: float = 0) -> float:
        if a <= 0:
            raise ValueError("Logarithm is not defined for values less than or equal to zero.")
        return math.log(a)
