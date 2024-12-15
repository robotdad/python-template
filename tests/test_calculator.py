"""Tests for the calculator package."""

import pytest

from calculator import Calculator, CalculatorError


def test_addition(calc: Calculator) -> None:
    """Test basic addition functionality."""
    result = calc.add(2, 3)
    assert result == 5
    assert len(calc.get_history()) == 1
    assert calc.get_history()[0].operation == "+"


def test_division(calc: Calculator) -> None:
    """Test basic division functionality."""
    result = calc.divide(6, 2)
    assert result == 3
    assert len(calc.get_history()) == 1
    assert calc.get_history()[0].operation == "/"


def test_division_by_zero(calc: Calculator) -> None:
    """Test that division by zero raises an error."""
    with pytest.raises(CalculatorError) as exc_info:
        calc.divide(1, 0)
    assert "Division by zero" in str(exc_info.value)
    assert len(calc.get_history()) == 0


def test_history_records_correctly(calc: Calculator) -> None:
    """Test that calculation history is recorded correctly."""
    calc.add(2, 3)
    calc.divide(10, 2)

    history = calc.get_history()
    assert len(history) == 2

    assert history[0].result == 5
    assert history[0].operation == "+"
    assert history[0].inputs == [2, 3]

    assert history[1].result == 5
    assert history[1].operation == "/"
    assert history[1].inputs == [10, 2]


def test_history_independence(calc: Calculator) -> None:
    """Test that getting history doesn't allow modifying the calculator's history."""
    calc.add(2, 3)
    history = calc.get_history()
    history.clear()  # Try to modify the returned history

    assert len(calc.get_history()) == 1  # Original history should be unchanged
