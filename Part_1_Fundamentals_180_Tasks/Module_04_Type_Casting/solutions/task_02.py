"""
Task 4.02: String to Float and Multiplication
EN: Convert string '6.28' to float and multiply by 3.
PL: Zamień napis '6.28' na liczbę zmiennoprzecinkową i pomnóż przez 3.
Standard: PEP 8 (<= 88 characters)
"""

float_str = "6.28"
result = float(float_str) * 3

print(f"Original: '{float_str}' | Multiplied: {result:.2f}")
