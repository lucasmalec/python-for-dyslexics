"""
Task 8.06: Docstring Documentation
EN: Add PEP 257 docstring explaining function behavior and parameters.
PL: Dodaj docstring do funkcji opisujący jej działanie.
Standard: PEP 8 (<= 88 characters)
"""

def compute_vat(amount: float, rate: float = 0.23) -> float:
    """Calculate the tax amount for a given net price.

    Args:
        amount: Net currency amount.
        rate: Tax decimal rate (defaults to 0.23).

    Returns:
        Calculated tax amount.
    """
    return amount * rate


print(f"Tax: {compute_vat(100.0):.2f}")
