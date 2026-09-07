"""
Task 4.12: Exception Handling on Invalid Conversion
EN: Try converting string 'abc' to int. Catch `ValueError` gracefully.
PL: Spróbuj zamienić napis 'abc' na `int`. Użyj `try/except`, aby przechwycić błąd.
Standard: PEP 8 (<= 88 characters)
"""

text = "abc"

try:
    num = int(text)
    print(f"Converted: {num}")
except ValueError:
    print(f"Safe error handle: '{text}' cannot be parsed into an integer.")
