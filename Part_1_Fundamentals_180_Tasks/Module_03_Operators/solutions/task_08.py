"""
Task 3.08: Logical OR
EN: Check if number 3 is greater than 10 OR less than 5.
PL: Sprawdź, czy liczba 3 jest większa od 10 lub mniejsza od 5.
Standard: PEP 8 (<= 88 characters)
"""

number = 3
is_matching = (number > 10) or (number < 5)

print(f"Is {number} > 10 or < 5? {is_matching}")
