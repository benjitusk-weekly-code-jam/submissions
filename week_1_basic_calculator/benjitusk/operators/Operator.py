# Author: Benji Tusk
from abc import ABC, abstractmethod


class Operator(ABC):
    """Base class for all mathmatical operators"""
    pass

    @property
    @abstractmethod
    def operator_sign(self) -> str:
        pass

    @property
    @abstractmethod
    def operator_name(self) -> str:
        pass

    @classmethod
    @abstractmethod
    def can_handle_expression(cls, expression: str) -> bool:
        pass

    @classmethod
    @abstractmethod
    def execute(cls, expression: str) -> float:
        pass
