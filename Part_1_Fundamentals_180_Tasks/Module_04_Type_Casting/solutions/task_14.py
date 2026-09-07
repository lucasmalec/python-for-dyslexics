"""
Task 4.14: Defensive safe_int Function
EN: Write function `safe_int(val)` returning parsed int or `None` on failure.
PL: Napisz funkcję `bezpieczna_int(napis)`, która zwraca `None`, jeśli
    konwersja się nie uda.
Standard: PEP 8 (<= 88 characters)
"""

def safe_int(value: str) -> int | None:
    """Safely convert a string to integer, returning None if invalid."""
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return None


print("safe_int('123'): ", safe_int("123"))
print("safe_int('invalid'):", safe_int("invalid"))
print("safe_int(None):  ", safe_int(None))
