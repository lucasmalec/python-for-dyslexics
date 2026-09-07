"""
Task 7.07: Return Values Over Side Effects
EN: Return results from functions with `return` instead of printing directly.
PL: W funkcji użyj `return` zamiast `print` – zwróć wynik, a nie wyświetlaj.
Standard: PEP 8 (<= 88 characters)
"""

def get_circle_circumference(radius: float) -> float:
    pi = 3.1415926535
    return 2 * pi * radius


radius_val = 7.5
circumference = get_circle_circumference(radius_val)
print(f"Radius: {radius_val} -> Circumference: {circumference:.2f}")
