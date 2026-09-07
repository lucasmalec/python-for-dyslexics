"""
Task 10.04: Float Parsing Guard
EN: Prompt for a decimal float and handle invalid string inputs.
PL: Poproś o liczbę zmiennoprzecinkową. Obsłuż błąd, jeśli użytkownik poda
    coś innego.
Standard: PEP 8 (<= 88 characters)
"""

try:
    val = float(input("Enter float: ").strip())
    print(f"Float accepted: {val}")
except ValueError:
    print("Error: Could not convert input to a floating-point number.")
