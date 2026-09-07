"""
Task 10.01: Integer Parsing with try/except
EN: Prompt for an integer and handle `ValueError` gracefully using `try/except`.
PL: Poproś użytkownika o liczbę całkowitą. Użyj `try/except` do obsługi `ValueError`.
Standard: PEP 8 (<= 88 characters)
"""

try:
    number = int(input("Enter an integer: ").strip())
    print(f"Valid integer entered: {number}")
except ValueError:
    print("Error: Input is not a valid integer.")
