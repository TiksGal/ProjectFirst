import math

class Calculator:
    def __init__(self, number_1, number_2) -> None:
        self.number_1 = number_1
        self.number_2 = number_2
    
    def add(self) -> float:
        return self.number_1 + self.number_2
    
    def subtract(self) -> float:
        return self.number_1 - self.number_2
    
    def multiply(self) -> float:
        return self.number_1 * self.number_2
    
    def divide(self) -> float:
        if self.number_2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.number_1 / self.number_2

class ScientificCalculator(Calculator):
    def __init__(self, number_1, number_2) -> None:
        super().__init__(number_1, number_2)
    
    def power(self) -> float:
        return self.number_1 ** self.number_2
    
    def sqrt(self) -> float:
        if self.number_1 < 0:
            raise ValueError("Cannot take square root of a negative number")
        return math.sqrt(self.number_1)
    
    def sin(self) -> float:
        return math.sin(self.number_1)
    
    def cos(self) -> float:
        return math.cos(self.number_1)
    
    def tan(self) -> float:
        return math.tan(self.number_1)