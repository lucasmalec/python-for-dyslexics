"""
Task 10.09: ZeroDivisionError Exception Handler
EN: Prompt for two numbers and handle `ZeroDivisionError` with try/except.
PL: Poproś o dwie liczby i wykonaj dzielenie. Obsłuż błąd dzielenia przez zero.
Standard: PEP 8 (<= 88 characters)
"""

try:
    a = float(input("Numerator: ").strip())
    b = float(input("Denominator: ").strip())
    result = a / b
    print(f"{a} / {b} = {result:.4f}")
except ZeroDivisionError:
    print("Math Error: Division by zero is undefined.")
except ValueError:
    print("Parse Error: Invalid numeric input.")
