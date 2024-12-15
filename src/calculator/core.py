"""Core calculator functionality."""

from typing import List

from pydantic import BaseModel


class CalculatorError(Exception):
    """Custom exception for calculator errors."""

    pass


class CalculationResult(BaseModel):
    """Model for storing calculation results with history."""

    result: float
    operation: str
    inputs: List[float]

    def __str__(self) -> str:
        return f"{' '.join(map(str, self.inputs))} {self.operation} = {self.result}"


class Calculator:
    """A simple calculator class demonstrating basic functionality."""

    def __init__(self) -> None:
        """Initialize the calculator with an empty history."""
        self.history: List[CalculationResult] = []

    def add(self, a: float, b: float) -> float:
        """Add two numbers and store the result in history.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of the two numbers
        """
        result = a + b
        self.history.append(
            CalculationResult(result=result, operation="+", inputs=[a, b])
        )
        return result

    def divide(self, a: float, b: float) -> float:
        """Divide first number by second number and store result in history.

        Args:
            a: Number to divide
            b: Number to divide by

        Returns:
            Result of division

        Raises:
            CalculatorError: If attempting to divide by zero
        """
        if b == 0:
            raise CalculatorError("Division by zero is not allowed")

        result = a / b
        self.history.append(
            CalculationResult(result=result, operation="/", inputs=[a, b])
        )
        return result

    def get_history(self) -> List[CalculationResult]:
        """Get the history of calculations.

        Returns:
            List of calculation results
        """
        return self.history.copy()
