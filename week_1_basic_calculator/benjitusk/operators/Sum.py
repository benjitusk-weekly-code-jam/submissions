from .Operator import Operator
from typing import final


@final
class Sum(Operator):
    @property
    def operator_sign(cls):
        return "+"

    @property
    def operator_name(cls):
        return "plus"

    @classmethod
    def can_handle_expression(cls, expression: str) -> bool:
        return super().can_handle_expression(expression)

    @classmethod
    def execute(cls, expression: str) -> float:
        return super().execute(expression)
