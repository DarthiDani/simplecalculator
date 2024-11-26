from operations.addition import Addition
from operations.subtraction import Subtraction
from operations.multiplication import Multiplication
from operations.division import Division
from operations.exponentiation import Exponentiation
from operations.square_root import SquareRoot
from operations.logarithm import Logarithm


class Calculator:
    def __init__(self):
        self.operations = {
            '+': Addition(),
            '-': Subtraction(),
            '*': Multiplication(),
            '/': Division(),
            '^': Exponentiation(),
            'sqrt': SquareRoot(),
            'log': Logarithm()
        }

    def calculate(self, a: float, operator: str, b: float = 0) -> float:
        if operator not in self.operations:
            raise ValueError(f"Unsupported operation: {operator}")
        operation = self.operations[operator]
        return operation.execute(a, b)


if __name__ == "__main__":
    calculator = Calculator()
    print("Welcome to the calculator!")
    print("Available operations: +, -, *, /, ^ (exponentiation), sqrt (square root), log (natural logarithm)")

    a = float(input("Enter the first number: "))

    while True:
        try:
            operator = input(f"Enter an operator (+, -, *, /, ^, sqrt, log): ")

            if operator == "sqrt":
                if a < 0:
                    raise ValueError("Cannot calculate the square root of a negative number.")
                result = calculator.calculate(a, operator)
                print(f"The result is: {result}")
                a = result
            elif operator == "log":
                if a <= 0:
                    raise ValueError("Logarithm is not defined for values less than or equal to zero.")
                result = calculator.calculate(a, operator)
                print(f"The result is: {result}")
                a = result
            else:
                b = float(input("Enter the second number: "))

                if operator == "/" and b == 0:
                    raise ValueError("Division by zero is not allowed.")

                result = calculator.calculate(a, operator, b)
                print(f"The result is: {result}")
                a = result

            cont = input("Do you want to perform another operation on this result? (yes/no): ")
            if cont.lower() != 'yes':
                next_step = input("Do you want to enter a new number or exit the program? (new/exit): ")
                if next_step.lower() == 'exit':
                    break
                elif next_step.lower() == 'new':
                    a = float(input("Enter the new number: "))

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
