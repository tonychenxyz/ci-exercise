"""Define modules for uncertainty calculations."""

from __future__ import annotations

import math
import sys
from typing import Self

if sys.version_info < (3, 13):
    from typing_extensions import deprecated
else:
    from warnings import deprecated


class LabUnc:
    """Representation of a floating point lab value with an uncertainty."""

    @staticmethod
    def combine(a: float, b: float) -> float:
        """
        Combine two uncertainties.

        Args:
            a: float
            b: float
        returns:
            float

        """
        return a + b

    rounding_rule = 1.0
    """
    This is the number to round at for display, lab rule is 1, particle physics uses
    3.54
    """

    def __init__(self, number: float, uncertainty: float = 0.0) -> None:
        """
        Construct an instance of the class.

        Args:
            number: float
            uncertainty: float

        """
        self.n = number
        self.s = abs(uncertainty)

    @property
    @deprecated("no longer needed")
    def ndigits(self) -> int:
        """Return the number of digits to round to."""
        v = math.ceil(-math.log10(self.s) + math.log10(self.rounding_rule))
        return max(v, 0)

    @property
    def max(self) -> float:
        """Return the maximum value given the uncertainty."""
        return self.n + self.s

    @property
    def min(self) -> float:
        """Return the minimum value given the uncertainty."""
        return self.n - self.s

    def __repr__(self) -> str:
        """Return the REPR of the class."""
        return f"{self.__class__.__name__}({self.n}, {self.s})"

    def __str__(self) -> str:
        """Return the string representation of the class."""
        return f"{self.n:0.{self.ndigits}f} ± {self.s:0.{self.ndigits}f}"

    def __eq__(self, other: object) -> bool:
        """Compare two instances of the class."""
        return abs(self.n - other.n) < 0.0000001 and abs(self.s - other.s) < 0.0000001

    def __add__(self: Self, other: LabUnc) -> Self:
        """Add two instances of the class."""
        return self.__class__(self.n + other.n, self.combine(self.s, other.s))

    def __sub__(self: Self, other: LabUnc) -> Self:
        """Subtract two instances of the class."""
        return self.__class__(self.n - other.n, self.combine(self.s, other.s))

    def __mul__(self: Self, other: LabUnc) -> Self:
        """Multiply two instances of the class."""
        C = self.n * other.n
        δC = C * self.combine(self.s / self.n, other.s / other.n)
        return type(self)(C, δC)

    def __truediv__(self: Self, other: LabUnc) -> Self:
        """Divide two instances of the class."""
        C = self.n / other.n
        δC = C * self.combine(self.s / self.n, other.s / other.n)
        return self.__class__(C, δC)

    def __pow__(self: Self, power: float) -> Self:
        """Raise an instance of the class to a power."""
        C = self.n**power
        δC = C * (power * self.s / self.n)
        return self.__class__(C, δC)


class StdUnc(LabUnc):
    """Representation of a floating point standard value with an uncertainty."""

    @staticmethod
    def combine(a: float, b: float) -> float:
        """
        Combine two uncertainties.

        Args:
            a: float
            b: float
        returns:
            float

        """
        return math.sqrt(a**2 + b**2)
