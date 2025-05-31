from .BinaryOperator import BinaryOperator
from typing import final
import math


@final
class Logarithm(BinaryOperator):

    def __init__(self, expr: str):
        self.operator_name = "mod"
        self.operator_sign = "%"
        super().__init__(expr)

    def _build_pattern(self):
        float_match = "[+-]?(?:[0-9]*[.])?[0-9]+"
        return f"log_({float_match})\\(({float_match})\\)"

    def _execute(self) -> None:
        self.result = math.log(self.rhs, self.lhs)
