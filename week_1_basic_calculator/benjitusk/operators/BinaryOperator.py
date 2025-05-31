from .Operator import Operator, CannotParseExpr
from abc import abstractmethod
import re


class BinaryOperator(Operator):

    def __init__(self, expr: str) -> None:
        self.lhs: float
        self.rhs: float
        self.result: float = 0
        self.operator_name: str
        self.operator_sign: str

        self._pattern = self._build_pattern()
        super().__init__(expr)

    def _build_pattern(self):
        float_match = "[+-]?(?:[0-9]*[.])?[0-9]+"
        operator_match = f"[{self.operator_sign}]"
        whitespaces = "\\s*"
        return f"({float_match}){whitespaces}{operator_match}{whitespaces}({float_match})"

    def _parse_expr(self):
        """Split expression into RHS and LHS"""
        try:
            [(lhs, rhs)] = re.findall(self._pattern, self.expression)
            self.lhs = float(lhs)
            self.rhs = float(rhs)
        except ValueError:
            raise CannotParseExpr(self.expression)

    @abstractmethod
    def _execute(self) -> None:
        pass
