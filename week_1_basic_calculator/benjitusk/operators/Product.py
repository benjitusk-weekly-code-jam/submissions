from .BinaryOperator import BinaryOperator
from typing import final


@final
class Product(BinaryOperator):
    """
    Represents the binary multiplication operator.

    The Product class inherits from BinaryOperator and implements the multiplication operation.
    It parses an expression string, extracts the left-hand side (lhs) and right-hand side (rhs) operands,
    and computes their product.
    """

    def __init__(self, expr: str):
        self.operator_name = "times"
        self.operator_sign = "*"
        super().__init__(expr)

    def _execute(self) -> None:
        self.result = self.lhs * self.rhs
