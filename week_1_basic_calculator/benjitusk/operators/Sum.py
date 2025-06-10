from .BinaryOperator import BinaryOperator
from typing import final


@final
class Sum(BinaryOperator):
    """
    Represents the binary addition operator.

    The Sum class inherits from BinaryOperator and implements the addition operation.
    It parses an expression string, extracts the left-hand side (lhs) and right-hand side (rhs) operands,
    and computes their sum.
    """

    def __init__(self, expr: str):
        self.operator_name = "plus"
        self.operator_sign = "+"
        super().__init__(expr)

    def _execute(self) -> None:
        self.result = self.lhs + self.rhs
