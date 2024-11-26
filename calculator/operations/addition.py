from .operation import Operation

class Addition(Operation):
    def execute(self, a: float, b: float) -> float:
        return a + b
