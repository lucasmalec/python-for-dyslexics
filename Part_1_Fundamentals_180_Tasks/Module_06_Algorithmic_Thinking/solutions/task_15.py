"""
Task 6.15: IPO Pattern: Triangle Area
EN: Calculate triangle area using formula: (base * height) / 2.
PL: Napisz program obliczający pole trójkąta ((podstawa * wysokość) / 2).
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
base = float(input("Enter triangle base: ").strip())
height = float(input("Enter triangle height: ").strip())

# 2. PROCESS
area = (base * height) / 2

# 3. OUTPUT
print(f"Triangle area: {area:.2f}")
