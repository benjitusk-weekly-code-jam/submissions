# Author: Benji Tusk
from abc import ABC, abstractmethod


class Operator(ABC):
    """Base class for all mathmatical operators"""

    def __init__(self, expr: str):
        self.expression = expr
        self._pattern: str
        self.result: float

    operator_sign: str
    operator_name: str

    @classmethod
    def can_handle_expression(cls, expression: str) -> bool:
        try:
            cls(expression)._parse_expr()
        except CannotParseExpr:
            return False
        return True

    @abstractmethod
    def _parse_expr(self) -> None:
        pass

    @abstractmethod
    def _execute(self) -> None:
        pass

    def calculate(self) -> float:
        self._parse_expr()
        self._execute()
        return self.result


class CannotParseExpr(Exception):
    def __init__(self, expression: str):
        self.expression = expression
        self.message = f"Cannot parse {expression=}"
        super().__init__(self.message)
