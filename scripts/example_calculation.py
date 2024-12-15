"""Example script demonstrating calculator usage."""

from calculator import Calculator


def main() -> None:
    """Run example calculations and show results."""
    calc = Calculator()

    # Perform some calculations
    print("Performing calculations...")
    result1 = calc.add(5, 3)
    print(f"5 + 3 = {result1}")

    result2 = calc.divide(10, 2)
    print(f"10 / 2 = {result2}")

    # Show calculation history
    print("\nCalculation history:")
    for calculation in calc.get_history():
        print(calculation)


if __name__ == "__main__":
    main()
