"""
Task 11.10: Exception Inspection
EN: Attempt `10 / 0` inside try/except and print error type and message.
PL: Spróbuj wykonać `10 / 0` i odczytaj typ błędu.
Standard: PEP 8 (<= 88 characters)
"""

try:
    _ = 10 / 0
except ZeroDivisionError as err:
    print(f"Caught Exception: {type(err).__name__} -> '{err}'")
