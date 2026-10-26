"""Defines tests for the StdUnc class."""

from uncertainties import ufloat

from unc import StdUnc


def test_add(ab):
    """Test addition of two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) + StdUnc(*b) == ufloat(*a) + ufloat(*b)


def test_sub(ab):
    """Test subtraction between two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) - StdUnc(*b) == ufloat(*a) - ufloat(*b)


def test_mul(ab):
    """Test multiplication between two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) * StdUnc(*b) == ufloat(*a) * ufloat(*b)


def test_div(ab):
    """Test division of two StdUnc instances."""
    a, b = ab
    assert StdUnc(*a) / StdUnc(*b) == ufloat(*a) / ufloat(*b)
