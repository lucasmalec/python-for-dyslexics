"""
Task 3.13: Quadratic Discriminant
EN: Calculate the discriminant delta for equation: a=1, b=4, c=4 (formula: b^2 - 4ac).
PL: Oblicz deltę dla równania: a=1, b=4, c=4 (wzór: b² - 4ac).
Standard: PEP 8 (<= 88 characters)
"""

a = 1
b = 4
c = 4

delta = (b ** 2) - (4 * a * c)
print(f"Equation parameters: a={a}, b={b}, c={c}")
print(f"Discriminant delta (b^2 - 4ac): {delta}")
