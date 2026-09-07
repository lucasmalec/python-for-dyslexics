"""
Task 10.12: Full try-except-else-finally Flow
EN: Implement complete `try/except/else/finally` control flow.
PL: Użyj bloku `try/except/else/finally` – w `else` wyświetl wynik,
    w `finally` napisz 'Koniec operacji'.
Standard: PEP 8 (<= 88 characters)
"""

try:
    val = int(input("Enter integer to double: ").strip())
except ValueError:
    print("Catch: Conversion error detected.")
else:
    print(f"Else: Doubled value is {val * 2}")
finally:
    print("Finally: End of operation cleanup.")
