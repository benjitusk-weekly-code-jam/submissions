from .BinaryOperator import BinaryOperator
from typing import final


@final
class Modulus(BinaryOperator):
    """
    Represents the binary modulus operator.

    The Modulus class inherits from BinaryOperator and implements the modulus operation.
    It parses an expression string, extracts the left-hand side (lhs) and right-hand side (rhs) operands,
    and computes their modulus (remainder of the division of lhs by rhs).
    """

    def __init__(self, expr: str):
        self.operator_name = "mod"
        self.operator_sign = "%"
        super().__init__(expr)

    def _execute(self) -> None:
        self.result = self.lhs % self.rhs
