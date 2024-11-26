from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass
