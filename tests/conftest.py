"""Pytest configuration and fixtures."""

import pytest

from calculator import Calculator


@pytest.fixture
def calc() -> Calculator:
    """Provide a fresh calculator instance for each test."""
    return Calculator()
