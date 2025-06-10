from .Operator import Operator, CannotParseExpr
from abc import abstractmethod
import re


class BinaryOperator(Operator):
    """
    Base class for binary mathematical operators.

    This class provides a framework for implementing binary operators (such as addition, subtraction, etc.)
    that operate on two floating-point operands parsed from a string expression.

    Attributes:
        lhs (float): The left-hand side operand.
        rhs (float): The right-hand side operand.
        result (float): The result of the operation. Defaults to 0.
        _pattern (str): The regular expression pattern used to parse the expression.

    Args:
        expr (str): The string expression to be parsed and evaluated.
    """

    def __init__(self, expr: str) -> None:
        self.lhs: float
        self.rhs: float
        self.result: float = 0

        self._pattern = self._build_pattern()
        super().__init__(expr)

    def _build_pattern(self):
        """Constructs a regular expression pattern to match the binary operation in the expression."""

        float_match = "[+-]?(?:[0-9]*[.])?[0-9]+"
        operator_match = f"[{self.operator_sign}]"
        whitespaces = "\\s*"
        return f"({float_match}){whitespaces}{operator_match}{whitespaces}({float_match})"

    def _parse_expr(self):
        """
        Parses the expression string to extract the left-hand side and right-hand side operands.
        Raises:
            CannotParseExpr: If the expression cannot be parsed into two operands.
        """

        try:
            [(lhs, rhs)] = re.findall(self._pattern, self.expression)
            self.lhs = float(lhs)
            self.rhs = float(rhs)
        except ValueError:
            raise CannotParseExpr(self.expression)

    @abstractmethod
    def _execute(self) -> None:
        """Executes the binary operation using the parsed operands."""
        pass
