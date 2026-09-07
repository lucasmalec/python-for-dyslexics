"""
Task 6.04: IPO Pattern: Distance Unit Converter
EN: Convert kilometers to miles (1 mile = 1.609344 km).
PL: Napisz program przeliczający kilometry na mile (1 mila = 1.609344 km).
Standard: PEP 8 (<= 88 characters)
"""

KM_PER_MILE = 1.609344

# 1. INPUT
kilometers = float(input("Enter distance in kilometers: ").strip())

# 2. PROCESS
miles = kilometers / KM_PER_MILE

# 3. OUTPUT
print(f"{kilometers:.2f} km is equal to {miles:.2f} miles.")
