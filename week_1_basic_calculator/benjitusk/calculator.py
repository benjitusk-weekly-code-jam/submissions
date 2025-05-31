# Author: Benji Tusk

from operators.Operator import Operator
from operators.Sum import Sum
from operators.Difference import Difference
from operators.Divide import Divide
from operators.Product import Product
from operators.Modulus import Modulus
from operators.Logarithm import Logarithm


class Calculator:

    supported_operators: list[type[Operator]] = [
        Sum, Difference, Divide, Product, Modulus, Logarithm]

    def __init__(self):
        self.expression: str = ""
        self.result: float | None = None
        self.get_input()

    def get_input(self):
        self.expression = input("Please enter a valid expression: ")
        op = self.__class__.get_op(self.expression)  # type: ignore
        if op is None:
            raise IllegalExpression(self.expression)

        op(self.expression).calculate()

    @classmethod
    def get_op(cls, expr: str) -> type[Operator] | None:
        eligible_ops = list(
            filter(lambda op: op.can_handle_expression(expr), cls.supported_operators))
        if len(eligible_ops) != 1:
            return None
        else:
            return eligible_ops[0]

    def calculate(self):
        op = self.__class__.get_op(self.expression)  # type: ignore
        if op is None:
            raise IllegalExpression(self.expression)

        self.result = op(self.expression).calculate()
        print("Executing calculate method")


class IllegalExpression(Exception):
    """Exception raised when an expression cannot be parsed by the Calculator

    Attributes:
        expression -- The expression that could not be parsed
    """

    def __init__(self, expression: str):
        self.message = f"The expression '{expression}' is illegal."
        super().__init__(self.message)
