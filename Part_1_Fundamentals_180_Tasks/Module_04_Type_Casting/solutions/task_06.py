"""
Task 4.06: Float String to Integer Pitfall
EN: Attempt `int('12.7')` and demonstrate two-step conversion `int(float('12.7'))`.
PL: Spróbuj zamienić napis '12.7' na `int`. Co się dzieje? Zapisz kod i zobacz efekt.
Standard: PEP 8 (<= 88 characters)
"""

raw_val = "12.7"

try:
    direct_int = int(raw_val)
    print(direct_int)
except ValueError as err:
    print(f"Direct int('{raw_val}') failed with: {err}")

# Safe two-step conversion:
converted = int(float(raw_val))
print(f"Two-step conversion int(float('{raw_val}')) produces: {converted}")
