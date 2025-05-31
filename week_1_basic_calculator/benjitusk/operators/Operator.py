# Author: Benji Tusk
from abc import ABC, abstractmethod


class Operator(ABC):
    """
    Abstract base class for mathematical operators in an expression calculator.

    Attributes:
        expression (str): The mathematical expression to be evaluated.
        _pattern (str): The pattern used to parse the expression (to be defined in subclasses).
        result (float): The result of the calculation.
        operator_sign (str): Symbol representing the operator (to be defined in subclasses).
        operator_name (str): Name of the operator (to be defined in subclasses).
    """

    def __init__(self, expr: str):
        self.expression = expr
        self._pattern: str
        self.result: float

    # The sign used to represent the operator, e.g., '+', '-', '*', '/'
    operator_sign: str
    # The name of the operator, e.g., 'addition', 'subtraction', etc.
    operator_name: str

    @classmethod
    def can_handle_expression(cls, expression: str) -> bool:
        """Class method to determine if the operator can handle the given expression."""
        try:
            cls(expression)._parse_expr()
        except CannotParseExpr:
            return False
        return True

    @abstractmethod
    def _parse_expr(self) -> None:
        """Method to parse the expression. Must be implemented in subclasses."""
        pass

    @abstractmethod
    def _execute(self) -> None:
        """Method to execute the operation. Must be implemented by subclasses."""
        pass

    def calculate(self) -> float:
        """Parses the expression, executes the operation, and returns the result."""
        self._parse_expr()
        self._execute()
        return self.result


class CannotParseExpr(Exception):
    """
    Exception raised when an expression cannot be parsed by an operator.
    Attributes:
        expression (str): The expression that could not be parsed.
        message (str): Explanation of the error.
    """

    def __init__(self, expression: str):
        self.expression = expression
        self.message = f"Cannot parse {expression=}"
        super().__init__(self.message)
