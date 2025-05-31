from .BinaryOperator import BinaryOperator
from typing import final


@final
class Divide(BinaryOperator):
    """
    Represents the binary division operator.

    The Divide class inherits from BinaryOperator and implements the division operation.
    It parses an expression string, extracts the left-hand side (lhs) and right-hand side (rhs) operands,
    and computes their quotient.
    """
    operator_name = "divide"
    operator_sign = "/"

    def __init__(self, expr: str):
        super().__init__(expr)

    def _execute(self) -> None:
        """Performs the division of lhs by rhs, storing the result.
        Raises:
            ZeroDivisionError: If rhs is zero, as division by zero is undefined.
        """
        self.result = self.lhs / self.rhs
