from .operation import Operation

class Multiplication(Operation):
    def execute(self, a: float, b: float) -> float:
        return a * b