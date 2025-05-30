from .Operator import Operator, CannotParseExpr
from typing import final
import re


@final
class Sum(Operator):

    def __init__(self, expr: str) -> None:
        self.lhs: float
        self.rhs: float
        self.result: float = 0
        self._pattern = Sum.__build_pattern()
        super().__init__(expr)

    @staticmethod
    def __build_pattern():
        float_match = "[+-]?(?:[0-9]*[.])?[0-9]+"
        operator_match = "[+]"
        whitespaces = "\\s*"
        return f"({float_match}){whitespaces}{operator_match}{whitespaces}({float_match})"

    @property
    def operator_sign(cls):
        return "+"

    @property
    def operator_name(cls):
        return "plus"

    def _parse_expr(self):
        """Split expression into RHS and LHS"""
        try:
            [(lhs, rhs)] = re.findall(self._pattern, self.expression)
            self.lhs = float(lhs)
            self.rhs = float(rhs)
        except ValueError:
            raise CannotParseExpr(self.expression)

    def _execute(self) -> None:
        self.result = self.lhs + self.rhs
