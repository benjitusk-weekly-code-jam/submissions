from .BinaryOperator import BinaryOperator
from typing import final
import math


@final
class Logarithm(BinaryOperator):
    """
    Represents the binary logarithm operator.

    The Logarithm class inherits from BinaryOperator and implements the logarithm operation.
    It parses an expression string, extracts the left-hand side (lhs) and right-hand side (rhs) operands,
    and computes the logarithm of rhs to the base of lhs.
    """

    def __init__(self, expr: str):
        self.operator_name = "log"
        self.operator_sign = "log_"
        super().__init__(expr)

    def _build_pattern(self):
        """
        Constructs a regular expression pattern to match the logarithm operation in the expression.
        Matches the format: log_(base)(value).
        The base and value are floating-point numbers, which can be positive or negative,
        and may include decimal points.
        """
        float_match = "[+-]?(?:[0-9]*[.])?[0-9]+"
        return f"log_({float_match})\\(({float_match})\\)"

    def _execute(self) -> None:
        self.result = math.log(self.rhs, self.lhs)
