"""
Task 4.11: String '0' Truthiness
EN: Convert string '0' to bool – analyze the returned boolean.
PL: Zamień napis '0' na `bool` – co otrzymasz?
Standard: PEP 8 (<= 88 characters)
"""

zero_str = "0"
is_true = bool(zero_str)

print(f"bool('{zero_str}') = {is_true}")
print("Explanation: Python evaluates non-empty strings as True regardless of characters.")
