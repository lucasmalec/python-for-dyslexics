"""
Task 7.09: Square Root on Secondary Number
EN: Prompt for an additional number and compute its square root.
PL: Zapytaj o dodatkową liczbę i wyświetl jej pierwiastek kwadratowy.
Standard: PEP 8 (<= 88 characters)
"""

num = float(input("Enter a positive number: ").strip())

if num >= 0:
    sqrt_val = num ** 0.5
    print(f"Square root of {num} is {sqrt_val:.4f}")
else:
    print("Cannot compute real square root of a negative number.")
