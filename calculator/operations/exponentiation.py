from .operation import Operation

class Exponentiation(Operation):
    def execute(self, a: float, b: float) -> float:
        return a ** b
