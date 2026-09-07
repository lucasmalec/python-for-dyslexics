"""
Task 4.05: User Float Input Sum
EN: Ask user for two decimal numbers as text, convert to float, and display sum.
PL: Poproś użytkownika o dwie liczby (jako tekst), przekonwertuj je na `float`
    i wyświetl ich sumę.
Standard: PEP 8 (<= 88 characters)
"""

raw_a = input("Enter first number: ").strip()
raw_b = input("Enter second number: ").strip()

sum_val = float(raw_a) + float(raw_b)
print(f"Sum of {raw_a} and {raw_b} is: {sum_val:.4f}")
