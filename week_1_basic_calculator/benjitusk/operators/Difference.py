from .BinaryOperator import BinaryOperator
from typing import final


@final
class Difference(BinaryOperator):

    def __init__(self, expr: str):
        self.operator_name = "minus"
        self.operator_sign = "-"
        super().__init__(expr)

    def _execute(self) -> None:
        self.result = self.lhs - self.rhs
