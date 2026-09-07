"""
Task 3.07: Logical AND
EN: Check if number 8 is greater than 5 AND simultaneously less than 12.
PL: Sprawdź, czy liczba 8 jest większa od 5 i jednocześnie mniejsza od 12.
Standard: PEP 8 (<= 88 characters)
"""

number = 8
is_valid = (number > 5) and (number < 12)

print(f"Is {number} > 5 and < 12? {is_valid}")
