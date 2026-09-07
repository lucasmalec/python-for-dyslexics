"""
Task 6.09: IPO Pattern: Trapezoid Area
EN: Calculate trapezoid area with formula: area = ((a + b) * h) / 2.
PL: Napisz program obliczający pole trapezu według wzoru: `P = ((a + b) * h) / 2`.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
base_a = float(input("Enter base a: ").strip())
base_b = float(input("Enter base b: ").strip())
height = float(input("Enter height: ").strip())

# 2. PROCESS
area = ((base_a + base_b) * height) / 2

# 3. OUTPUT
print(f"Trapezoid area: {area:.2f}")
