"""
Task 6.03: IPO Pattern: BMI Calculator
EN: Calculate BMI (weight in kg, height in m) using formula: weight / height^2.
PL: Napisz program obliczający BMI (waga w kg, wzrost w m) – wzór: `waga / wzrost²`.
Standard: PEP 8 (<= 88 characters)
"""

# 1. INPUT
weight_kg = float(input("Enter weight in kg: ").strip())
height_m = float(input("Enter height in meters (e.g. 1.75): ").strip())

# 2. PROCESS
bmi = weight_kg / (height_m ** 2)

# 3. OUTPUT
print(f"Calculated BMI: {bmi:.2f}")
