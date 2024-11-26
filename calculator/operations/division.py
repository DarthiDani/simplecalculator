from .operation import Operation

class Division(Operation):
    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b