from .BinaryOperator import BinaryOperator
from typing import final


@final
class Difference(BinaryOperator):
    """
    Represents the binary subtraction operator.

    The Difference class inherits from BinaryOperator and implements the subtraction operation.
    It parses an expression string, extracts the left-hand side (lhs) and right-hand side (rhs) operands,
    and computes their difference.
    """

    operator_name = "minus"
    operator_sign = "-"

    def __init__(self, expr: str):
        super().__init__(expr)

    def _execute(self) -> None:
        self.result = self.lhs - self.rhs
